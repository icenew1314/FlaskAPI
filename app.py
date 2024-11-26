from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 加载 JSON 文件
with open("final.json", "r") as f:
    data = json.load(f)

@app.route('/')
def home():
    return "Welcome to the Flask API! Use /questions or /search to interact with the API."

# GET 接口：获取所有问题
@app.route('/questions', methods=['GET'])
def get_questions():
    questions = [item['prompt'] for item in data]
    return jsonify(questions), 200

# POST 接口：根据关键词查询答案
@app.route('/search', methods=['POST'])
def search():
    keyword = request.json.get('keyword', '').lower()
    if not keyword:
        return jsonify({"error": "Please provide a keyword"}), 400

    results = [item for item in data if keyword in item['prompt'].lower()]
    if not results:
        return jsonify({"message": "No matching results found"}), 404

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
