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

## .env
``` t
OPENAI_API_KEY={key}

MARIADB_HOST="db"
MARIADB_PORT="3306"
MARIADB_ROOT_PASSWORD="1234"
MARIADB_DATABASE="mydb"
MARIADB_USER="dev"
MARIADB_PASSWORD="1234"

# 저장소 연결용
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_ID=""
AWS_REGION=""
S3_BUCKET_NAME=""
```

## docker
docker-compose-dev.yml :: 개발용

## 방학때 하면 좋을 것
1. HTTPS 설정 (SSL 인증서)
    - IP주소는 인증서 발급 X
    - Domain Name(ex: naver.com)
      - AWS Route53
      - 가비아
  * http://cs-cloud.com 접속 가능
  - "cs-cloud.com"으로 SSL 인증서 발급(Certbot)
    tip : certbot 스케줄링 도커 컨테이너
  - NginX 설정
    - + 443(https) 추가
    - 만약 80으로 접속을 하면, 443으로 접속하게 해야함