# dramacomany
## 환경 설정
python3 -m venv venv

pip3 install flask

sqlite3 database.db < schema.sql

## 실행
python3 drama.py

## 테스트
https://www.getpostman.com/
(pytest 적용하고 싶었으나...)

## API 
### 가입
/user/signup POST

{
    "email" : "passenger01@dramacompany.com",
    "password" : "password",
    "is_driver": 1
}

### 로그인
/user/signin POST

{
    "email" : passenger01@dramacompany.com",
    "password" : "password"
}

### 배차 요청 리스트
/call/list GET

### 승객이 택시 배차 요청
/call/passenger POST

{
    "user_id" : 1,
    "address" : "서울시 강남구"
}

### 택시 기사가 배차 신청
/call/driver POST

{
    "user_id" : 2,
    "call_id" : 1
}
