#drama.py
from flask import Flask
from flask import request
import models as dbHandler
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# 가입
@app.route("/signup")
def signup():
   if request.method=='POST':
       email = request.form['email']
       password = request.form['password']
       dbHandler.insertUser(email, password)

# 로그인
@app.route("/signin")
def signin():
   if request.method=='POST':
       return dbHandler.selectUserByEmail(email)

# 전체 배차 요청리스트
@app.route("/request/list")
def requestList():
    return dbHandler.selectRequestList

# 승객이 택시 배차 요청
@app.route("/request/passenger")
def requestPassenger():
    passenger = request.form['passenger']
    address = request.from['address']
    insertRequest(passenger, address):

# 택시 기사가 리스트 중에 원하는 요청에 대하여 배차 요청
@app.route("/request/driver")
def requestDriver():
    request_id = request.form['request_id']
    driver = request.form['driver']
    # 트랜잭션 필요 ㅠㅠ
    request = selectRequestById(request_id):
    # 배차된 기사가 없으면 성공
    updateRequest(request_id, driver):

if __name__ == "__main__":
    app.run(debug=True)
