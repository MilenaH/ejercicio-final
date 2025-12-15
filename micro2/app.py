from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def data():
    return jsonify({
        "service": "micro2",
        "message": "respuesta desde micro2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)