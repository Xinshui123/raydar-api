# 使用Flask提供数据API:
import json
from flask import Flask, jsonify, request
from flask_cors import CORS  # 导入CORS模块
from scraper import main as new


app = Flask(__name__)
CORS(app)


# with open("test.json") as f:
#     all_data = json.load(f)
all_data = {}


@app.route("/api/endpoint", methods=["POST"])
def receive_data():
    global all_data
    data = request.json  # 获取前端发送的JSON数据
    # 在这里处理数据
    if data:
        key1_value = data.get("key1")
        all_data = {}  # 重置之前的内容
        all_data = new(key1_value)  # 直接覆盖之前的数据
        return {"message": "Data received successfully", "key1": key1_value}
    else:
        return {"message": "No data received"}, 400  # 返回400状态码表示请求无效


@app.route("/api/endpoint")
def data():
    print("API is Running")
    return jsonify(all_data)


@app.route("/")
def hello_world():
    return "Hello, World!"

