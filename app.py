from flask import Flask, request, render_template

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
        res = num1 + num2
    elif operation=='Multiply':
        res = num1 * num2
    elif operation=='Division':
        res = num1 / num2
    else:
        res = num1 - num2
    return res


print(__name__)

if __name__ == '__main__':
    app.run()
