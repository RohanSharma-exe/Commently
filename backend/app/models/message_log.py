from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from datetime import datetime
from app.core.database import Base


class MessageLog(Base):
    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, index=True)

    comment_event_id = Column(Integer, ForeignKey("comment_events.id"), nullable=False)
    recipient_id = Column(String, nullable=False)
    message_text = Column(String, nullable=False)

    status = Column(String, nullable=False)  # sent | failed
    sent_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("comment_event_id", name="uq_message_per_comment"),
    )
