# dramacomany
## 환경 설정
python3 -m venv venv

pip3 install flask

sqlite3 database.db < schema.sql

## 실행
python3 drama.py

## 테스트
postman을 활용하여 테스트(pytest 적용하고 싶었으나...)

https://www.getpostman.com/

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
response LIST

[ 
    call_id, passenger_id, address, driver_id(배차 안 되면 null), 배차요청시간, 배차완료시간(배차 안 되면 null)
]

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
