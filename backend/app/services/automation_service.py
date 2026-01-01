from sqlalchemy.orm import Session
from app.models.automation_rule import AutomationRule
from app.models.message_log import MessageLog
from app.models.comment_event import CommentEvent


def match_rule(rule: AutomationRule, comment_text: str) -> bool:
    if rule.trigger_type == "any":
        return True
    if rule.trigger_type == "keyword" and rule.keyword:
        return rule.keyword.lower() in comment_text.lower()
    return False


def process_comment_event(db: Session, event: CommentEvent):
    rules = db.query(AutomationRule).filter(
        AutomationRule.instagram_account_id == event.instagram_account_id,
        AutomationRule.ig_post_id == event.ig_post_id,
        AutomationRule.is_active.is_(True),
    ).all()

    for rule in rules:
        if not match_rule(rule, event.comment_text):
            continue

        already_sent = db.query(MessageLog).filter(
            MessageLog.comment_event_id == event.id
        ).first()

        if already_sent:
            return "dm_already_sent"

        # MOCK DM SENDING (Step 8 = real Meta API)
        message_text = rule.message_template

        log = MessageLog(
            comment_event_id=event.id,
            recipient_id=event.commenter_id,
            message_text=message_text,
            status="sent",
        )

        db.add(log)
        db.commit()

        return "dm_sent"

    return "no_matching_rule"
