from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """ Multiply search parameters a, b and return result """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a, b)

    return str(sum)

@app.route('/sub')
def subtract_nums():
    """ Subtract search parameters a, b and return result """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    difference = sub(a, b)

    return str(difference)

@app.route('/mult')
def multiply_nums():
    """ Multiply search parameters a, b and return result """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    product = mult(a, b)

    return str(product)

@app.route('/div')
def divide_nums():
    """ Divide search parameters a, b and return result """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    dividend = div(a, b)

    return str(dividend)

# FURTHER STUDY

opers = {
    'add' : add(a, b),
    'sub' : sub(a, b),
    'mult' : mult(a, b),
    'div' : div(a, b)
}

@app.route('/math/<oper>')
def do_math(oper):
    """ Perform math operation based on path parameter and search parameters a, b """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(opers[oper])







