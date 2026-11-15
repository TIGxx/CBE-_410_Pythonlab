from flask import Flask, request, jsonify
app = Flask(__name__)
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/greet')
def greet():
    name = request.args.get('name', 'student')
    return jsonify(message=f'Hello, {name[:40]}!')
@app.get('/calculate')
def calculate():
    operation = request.args.get('operation', 'add')
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)

    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None
    }

    if operation not in operations:
        return jsonify(error='Unsupported operation'), 400

    if operation == 'divide' and b == 0:
        return jsonify(error='Cannot divide by zero'), 400

    return jsonify(result=operations[operation])