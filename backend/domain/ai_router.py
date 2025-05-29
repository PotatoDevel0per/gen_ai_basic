from fastapi import APIRouter
from schema.image_schema import PromptRequest, PromptResponse
from datetime import datetime
import uuid
from service.ai_service import AIService

router = APIRouter(prefix="/api")

@router.post("/image", response_model=PromptResponse)
async def gen_image(req: PromptRequest):
    print(f"전달받은 프롬프트: {req}")
    unique_id = str(uuid.uuid4())
    print(f">> unique_id: {unique_id}")

    current_time = datetime.now() # 이미지 생성 날짜
    ai_service = AIService()


    return {"url": ""}
