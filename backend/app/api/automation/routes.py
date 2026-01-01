from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.automation_rule import AutomationRule
from app.models.instagram_account import InstagramAccount
from app.api.automation.schemas import AutomationRuleCreate

router = APIRouter(prefix="/automation", tags=["Automation"])


@router.post("/rules")
def create_rule(
    data: AutomationRuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ig_account = db.query(InstagramAccount).filter(
        InstagramAccount.user_id == current_user.id
    ).first()

    if not ig_account:
        raise HTTPException(status_code=400, detail="Instagram account not connected")

    rule = AutomationRule(
        instagram_account_id=ig_account.id,
        ig_post_id=data.ig_post_id,
        trigger_type=data.trigger_type,
        keyword=data.keyword,
        message_template=data.message_template,
    )

    db.add(rule)
    db.commit()
    db.refresh(rule)

    return {"rule_id": rule.id}
