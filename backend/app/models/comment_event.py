from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from datetime import datetime

from app.core.database import Base


class CommentEvent(Base):
    __tablename__ = "comment_events"

    id = Column(Integer, primary_key=True, index=True)

    instagram_account_id = Column(Integer, ForeignKey("instagram_accounts.id"), nullable=False)

    ig_comment_id = Column(String, nullable=False)
    ig_post_id = Column(String, nullable=False)
    commenter_id = Column(String, nullable=False)

    comment_text = Column(String, nullable=False)
    received_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("ig_comment_id", name="uq_ig_comment_id"),
    )
