from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/gethello", methods =['GET'])
def get_hello():
    return jsonify({"message": "Hello world!"})

@app.route("/sendhello", methods =['POST'])
def send_hello():
    data = request.get_json()
    return jsonify({"status": "message received!", "your_message": data['message']}),
200


if __name__ == '__main__':
    app.run(debug=True)