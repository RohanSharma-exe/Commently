from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
import json

from app.core.config import settings
from app.core.dependencies import get_db
from app.services.webhook_service import verify_meta_signature
from app.models.comment_event import CommentEvent
from app.services.automation_service import process_comment_event

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])


@router.get("/instagram")
def verify_webhook(
    hub_mode: str | None = None,
    hub_challenge: str | None = None,
    hub_verify_token: str | None = None,
):
    """
    Meta webhook verification handshake
    """
    if hub_mode == "subscribe" and hub_verify_token == "verify_token":
        return int(hub_challenge)

    raise HTTPException(status_code=403, detail="Verification failed")


@router.post("/instagram")
async def receive_instagram_webhook(
    request: Request,
    db: Session = Depends(get_db),
):
    raw_body = await request.body()

    if not raw_body:
        raise HTTPException(status_code=400, detail="Empty request body")

    # Signature check (skip in dev)
    if settings.ENVIRONMENT != "development":
        signature = request.headers.get("X-Hub-Signature-256")
        if not verify_meta_signature(raw_body, signature, settings.JWT_SECRET):
            raise HTTPException(status_code=401, detail="Invalid signature")

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    # TEMP simplified parsing
    try:
        entry = payload["entry"][0]
        change = entry["changes"][0]["value"]

        ig_comment_id = change["comment_id"]
        ig_post_id = change["media_id"]
        commenter_id = change["from"]["id"]
        comment_text = change["text"]
        ig_account_id = 1  # TEMP mapping
    except KeyError:
        raise HTTPException(status_code=400, detail="Malformed webhook payload")

    exists = db.query(CommentEvent).filter(
        CommentEvent.ig_comment_id == ig_comment_id
    ).first()

    if exists:
        return {"status": "duplicate_ignored"}

    event = CommentEvent(
        instagram_account_id=ig_account_id,
        ig_comment_id=ig_comment_id,
        ig_post_id=ig_post_id,
        commenter_id=commenter_id,
        comment_text=comment_text,
    )

    db.add(event)
    db.commit()

    db.refresh(event)

    result = process_comment_event(db, event)

    return {
        "status": "comment_received",
        "automation_result": result,
        }
