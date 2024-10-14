#pip install flask
from flask import Flask, render_template ,request
import requests
import json
# pip install flask-cors
from flask_cors import CORS

app = Flask(__name__)
# 모두 허용
CORS(app)

@app.route("/")
def index():
    return "Hello,Nick"

@app.route("/Hello")
def hello():
    #jinja2 템플릿 언어로 데이터로 매핑됨.,
    return render_template("hello.html", content ="전달 내용", name = "pangsu")

@app.route("/coin",method=['GET','POST'])
def coin():
    if request.method =='POST':
        print("post 요청됨")
        data = json.loads(request.get_json())
        print(data)
        res = requests.get("http://api.upbit.com/v1/ticker?markets="+ data['market'])
        return res.content
    elif request.method =='GET':
        res = requests.get("https:api.upbit.com/v1/market/all")
        coin_list = json.loads(res.content)
        return render_template("coin.html", coin=coin_list)


if __name__ =='__main__':
    ## app.run(debug=True)
    # ip 포트 변경
    app.run(debug=True, port=5500, host="0.0.0.0")
