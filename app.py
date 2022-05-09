from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"response": "OK", "code": 200})

@app.route("/doublesize", methods=['POST'])
def order():
    json_data = request.get_json()
    print("Data to be transformed is: ", json_data)
    json_data["size"] = json_data["size"] * 2
    print("Data has been transformed: ", json_data)
    return jsonify({"response": json_data, "code": 200})

if __name__ == '__main__':
    app.run(debug=True)