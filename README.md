# dramacomany
## 환경 설정
python3 -m venv venv

pip3 install flask

sqlite3 database.db < schema.sql

## 실행
python3 drama.py

## API 
### 가입
/signup POST
{
    "email" : "passenger01@dramacompany.com",
    "password" : "password",
    "is_driver": 1
}

### 로그인
/signin POST
{
    "email" : passenger01@dramacompany.com",
    "password" : "password",
}

### 배차 요청 리스트
/call/list GET

### 승객이 택시 배차 요청
/call/passenger
{
    "user_id" : 1
    "address" : "서울시 강남구"
}

### 택시 기사가 배차 신청
/call/driver
{
    "user_id" : 2
    "call_id" : 1
}
