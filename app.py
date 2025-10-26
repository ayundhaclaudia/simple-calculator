from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo dari Kalkulator Sederhana + Jenkins + Docker!"

@app.route('/calc', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        op = request.args.get('op')

        if op == 'tambah':
            result = a + b
        elif op == 'kurang':
            result = a - b
        elif op == 'kali':
            result = a * b
        elif op == 'bagi':
            result = a / b
        else:
            return jsonify({'error': 'Operator tidak dikenal. Gunakan tambah, kurang, kali, atau bagi.'})

        return jsonify({'hasil': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
