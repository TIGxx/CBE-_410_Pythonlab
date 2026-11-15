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
    expression = request.args.get('expression', '1+1')
    result = eval(expression)
    return jsonify(result=result)