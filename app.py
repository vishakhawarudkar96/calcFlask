from flask import Flask, request, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask"


@app.route('/cal', methods = ["GET"])
def math_operator():
    operation = request.json['operation']
    num1 = request.json['num1']
    num2 = request.json['num2']
    if operation=='add':
        res = int(num1) + int(num2)
    elif operation=='Multiply':
        res = int(num1) * int(num2)
    elif operation=='Division':
        res = int(num1) / int(num2)
    else:
        res = int(num1) - int(num2)
    return jsonify(res)


print(__name__)

if __name__ == '__main__':
    app.run()
