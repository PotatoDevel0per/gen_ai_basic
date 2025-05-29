from fastapi import APIRouter
from schema.image_schema import PromptRequest, PromptResponse

router = APIRouter(prefix="/api")

@router.post("/image", response_model=PromptResponse)
async def gen_image(req: PromptRequest):
    print(f"전달받은 프롬프트: {req}")
    return {"url": ""}
