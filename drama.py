#drama.py
from flask import Flask, jsonify, request
import models as dbHandler
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# 가입
@app.route("/signup", methods=["POST"])
def signup():
    if request.method=='POST':
        email = request.json['email']
        password = request.json['password']
        is_driver = request.json['is_driver']
        user = dbHandler.selectUserByEmail(email)
        if user:
            # 동일 메일 존재 에러처리
            return "이메일이 존재합니다", 400
        else:
            dbHandler.insertUser(email, password, is_driver)
            user = dbHandler.selectUserByEmail(email)
            return jsonify(user_id=user[0]), 200

# 로그인
@app.route("/signin", methods=["POST"])
def signin():
    email = request.json['email']
    password = request.json['password']
    user = dbHandler.selectUserByEmail(email)
    if user and user[2] == password:
        # 성공
        return jsonify(user_id=user[0]), 200
    else:
        # 에러
        return "로그인 실패", 400

# 전체 배차 요청리스트
@app.route("/call/list", methods=["GET"])
def callList():
    # driver 가 null 이면 배차되지 않은 것으로 클라이언트에서 처리하도록 설득..;;
    callList = dbHandler.selectCallList()
    if (callList):
        return jsonify(list(callList)), 200
    else:
        return "배차 요청이 없습니다", 400

# 승객이 택시 배차 요청
# 인증 필요
@app.route("/call/passenger", methods=["POST"])
def passengerCall():
    passenger = request.json['user_id']
    address = request.json['address']
    dbHandler.insertCall(passenger, address)
    return "배차요청하였습니다", 200

# 택시 기사가 리스트 중에 원하는 요청에 대하여 배차 요청
# 인증 필요
@app.route("/call/driver", methods=["POST"])
def driverDispatch():
    call_id = request.json['call_id']
    driver = request.json['user_id']
    # 트랜잭션 필요 ㅠㅠ
    call = dbHandler.selectCallById(call_id)
    if call[3]:
        return "이미 배차되었습니다", 400
    else:
        # 배차된 기사가 없으면 성공
        dbHandler.updateCall(call_id, driver)
        return "배차완료되었습니다", 200

if __name__ == "__main__":
    app.run(debug=True)
