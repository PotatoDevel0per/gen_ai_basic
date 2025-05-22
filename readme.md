# 개요
- 본 Repo는 클라우드 및 가상화 실습 수업이다.

# 환경설정

## requirement.txt
``` txt
requests 
python-dotenv
langchain-community
langchain-openai
langchain <- LLM 모델을 독립적으로 사용할 수 있음>
langgraph <구조 그릴 때 사용, 각 노드들을 langchain으로 구성>
openpyxl <- pandas를 사용하기 위해 가져와야함>
pandas
numpy
```
## venv 실행
`./venv/bin/activate` :: 가상환경 실행
`pip install -r requirement.txt` :: 라이브러리 다운로드
