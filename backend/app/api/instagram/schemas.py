from pydantic import BaseModel


class InstagramConnectResponse(BaseModel):
    connect_url: str


class InstagramCallbackPayload(BaseModel):
    code: str
