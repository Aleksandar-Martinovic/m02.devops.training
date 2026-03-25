from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    #raise NotImplementedError("Implement home endpoint using TDD")
    return jsonify({"message": "Welcome to the Flask App!"})


@app.route("/health")
def health():
    #raise NotImplementedError("Implement health endpoint using TDD")
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    #raise NotImplementedError("Implement add endpoint using TDD")
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = a + b
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = a - b
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = a * b
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    result = a / b
    return jsonify({"result": result})

#@app.route("/history", methods=['GET'])
#def history():
#    # This is a placeholder implementation. In a real application, you would store and retrieve the history of operations.
#    return jsonify([])


if __name__ == "__main__":
    app.run(debug=True)
