from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola desde  1 Microservicio 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
