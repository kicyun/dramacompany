#drama.py
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import models as dbHandler

app = Flask(__name__)
# utf8 처리
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "Hello DramaCompany!"

# 가입
@app.route("/user/signup", methods=["POST"])
def signup():
    try:
        email = request.json['email']
        password = generate_password_hash(request.json['password'])
        is_driver = request.json['is_driver']
        user = dbHandler.selectUserByEmail(email)
        if user:
            # 동일 메일 존재 에러처리
            return jsonify({'error':'이메일이 존재합니다'}), 400
        else:
            dbHandler.insertUser(email, password, is_driver)
            user = dbHandler.selectUserByEmail(email)
            return jsonify(user_id=user[0]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 로그인
@app.route("/user/signin", methods=["POST"])
def signin():
    try:
        email = request.json['email']
        password = request.json['password']
        user = dbHandler.selectUserByEmail(email)
        if user and check_password_hash(user[2], password):
            # 성공
            return jsonify(user_id=user[0]), 200
        else:
            # 에러
            return jsonify({'error': '로그인 실패'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 전체 배차 요청리스트
@app.route("/call/list", methods=["GET"])
def callList():
    try:
        # driver 가 null 이면 배차되지 않은 것으로 클라이언트에서 처리하도록 설득..;;
        callList = dbHandler.selectCallList()
        if (callList):
            return jsonify(list(callList)), 200
        else:
            return jsonify({'error': '배차 요청이 없습니다'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 승객이 택시 배차 요청
# 인증 필요 ㅠㅠ 
@app.route("/call/passenger", methods=["POST"])
def passengerCall():
    try:
        passenger = request.json['user_id']
        address = request.json['address']
        user = dbHandler.selectUserById(passenger)
        # SQLAlchemy 쓸 껄 ㅠㅠ
        # 승객인지 체크
        if user and user[3] == 0:
            dbHandler.insertCall(passenger, address)
            return jsonify({'message': '배차요청하였습니다'}), 200
        else:
            return jsonify({'error': '승객이 아닙니다'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 택시 기사가 리스트 중에 원하는 요청에 대하여 배차 요청
# 인증 필요
@app.route("/call/driver", methods=["POST"])
def driverDispatch():
    try:
        call_id = request.json['call_id']
        driver = request.json['user_id']
        user = dbHandler.selectUserById(driver)
        # 기사인지 체크
        if user and user[3] == 1:
            # 배차된 기사가 없으면 성공
            ret = dbHandler.updateCall(call_id, driver)
            if ret < 0:
                return jsonify({'error': '이미 배차되었습니다'}), 400
            else:
                return jsonify({'message': '배차완료되었습니다'}), 200
        else:
            return jsonify({'error': '택시 기사가 아닙니다'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
