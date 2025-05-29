from pydantic import BaseModel # type check

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    url: str