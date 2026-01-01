import hmac
import hashlib


def verify_meta_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verifies X-Hub-Signature-256 header from Meta
    """
    if not signature or not signature.startswith("sha256="):
        return False

    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(f"sha256={expected}", signature)
