from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class AutomationRule(Base):
    __tablename__ = "automation_rules"

    id = Column(Integer, primary_key=True, index=True)

    instagram_account_id = Column(Integer, ForeignKey("instagram_accounts.id"), nullable=False)
    ig_post_id = Column(String, nullable=False)

    trigger_type = Column(String, nullable=False)  # "any" | "keyword"
    keyword = Column(String, nullable=True)

    message_template = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
