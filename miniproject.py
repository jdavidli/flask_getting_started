from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    data = {
    "name": "David"
    }
    return jsonify(data)

@app.route("/hello/<name>", methods=["GET"])
def getData(name):
    data2 = {
    "message": "Hello there, %s" % name
    }
    return jsonify(data2)

@app.route("/distance", methods=["POST"])
def distance():
    dist = request.get_json()
    dist["distance"] = ((dist["a"][0]-dist["b"][0])**2+(dist["a"][1]-dist["b"][1])**2)**0.5
    print(dist)
    return jsonify(dist)


if __name__ == '__main__':
    app.run(debug=True)
