from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator Sederhana</title>
    <style>
        body { font-family: Arial; margin: 50px; text-align: center; }
        input, select { padding: 8px; margin: 5px; }
        button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; }
    </style>
</head>
<body>
    <h2>Kalkulator Sederhana</h2>
    <form method="POST">
        <input type="number" name="num1" step="any" placeholder="Angka 1" required>
        <select name="operator">
            <option value="+">+</option>
            <option value="-">−</option>
            <option value="*">×</option>
            <option value="/">÷</option>
        </select>
        <input type="number" name="num2" step="any" placeholder="Angka 2" required>
        <button type="submit">Hitung</button>
    </form>

    {% if result is not none %}
        <h3>Hasil: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operator = request.form["operator"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Tidak bisa dibagi 0"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
