from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.instagram_account import InstagramAccount


def connect_instagram_account(
    db: Session,
    user_id: int,
    ig_account_id: str,
    username: str,
    access_token: str,
):
    account = InstagramAccount(
        user_id=user_id,
        ig_account_id=ig_account_id,
        username=username,
        access_token=access_token,
        token_expires_at=datetime.utcnow() + timedelta(days=60),
    )

    db.add(account)
    db.commit()
    db.refresh(account)
    return account
