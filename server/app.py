#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5559, debug=True)



@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f'<h1>{title}</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print (input_string)
    return input_string

@app.route('/count/<int:num>')
def count(num):
    numbers = "\n".join(str(i) for i in range(num+1))
    return numbers


# Define the math route with three parameters: num1, operation, and num2
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    # Perform the specified operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, and %."

    return str(result)
