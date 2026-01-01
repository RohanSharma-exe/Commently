from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.services.instagram_service import connect_instagram_account
from app.api.instagram.schemas import InstagramConnectResponse

router = APIRouter(prefix="/instagram", tags=["Instagram"])


@router.get("/connect", response_model=InstagramConnectResponse)
def start_instagram_connect(current_user: User = Depends(get_current_user)):
    # TEMPORARY (mock OAuth URL)
    fake_state = str(uuid4())

    connect_url = (
        "https://www.facebook.com/v19.0/dialog/oauth"
        "?client_id=FAKE_APP_ID"
        "&redirect_uri=http://localhost:8000/instagram/callback"
        "&scope=instagram_basic,instagram_manage_messages"
        f"&state={fake_state}"
    )

    return {"connect_url": connect_url}


@router.get("/callback")
def instagram_callback(
    code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    TEMPORARY:
    - Normally exchange `code` with Meta
    - For now we simulate success
    """

    if not code:
        raise HTTPException(status_code=400, detail="Missing code")

    # MOCK DATA (will be replaced later)
    ig_account_id = "mock_ig_12345"
    username = "mock_instagram_user"
    access_token = "mock_access_token"

    account = connect_instagram_account(
        db=db,
        user_id=current_user.id,
        ig_account_id=ig_account_id,
        username=username,
        access_token=access_token,
    )

    return {
        "message": "Instagram account connected",
        "instagram_account_id": account.id,
        "username": account.username,
    }
