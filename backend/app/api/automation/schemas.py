from pydantic import BaseModel


class AutomationRuleCreate(BaseModel):
    ig_post_id: str
    trigger_type: str  # "any" | "keyword"
    keyword: str | None = None
    message_template: str
