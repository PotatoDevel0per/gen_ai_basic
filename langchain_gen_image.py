import os
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

# 이미지 생성 서비스 프로세스
# 1. User Prompt 
# 2. LLM -> User Prompt 확장
# 3. LLM -> 확장 Prompt 번역
# 4. DALL-E3 -> 이미지 생성 요청

openai_api_key = os.getenv("OPENAI_API_KEY")

# 1. .env 파일을을 찾고 로드함
_ = load_dotenv(find_dotenv()) 

# 2. LLM 모델 생성
llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0,
    openai_api_key = openai_api_key,
)

# 3. DALL-E3 모델 생성
client = OpenAI(api_key =openai_api_key)