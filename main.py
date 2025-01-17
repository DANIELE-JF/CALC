from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    n1 = request.args.get("n1", type=int)
    n2 = request.args.get("n2", type=int)
    operator = request.args.get("operator")
    
    if n1 is None or n2 is None or operator is None:
        return "Error: Missing required query parameters (n1, n2, operator)."

    result = None
    if operator == 'tambah':
        result = n1 + n2
    elif operator == 'kurang':
        result = n1 - n2
    elif operator == 'kali':
        result = n1 * n2
    elif operator == 'bagi':
        if n2 == 0:
            return "Error: Division by zero is not allowed."
        result = n1 / n2
    else:
        return f"Error: Unsupported operator {operator}"

    return render_template("cacl.html", n1=n1, n2=n2, operator=operator, result=result)

if __name__ == '__main__':
    app.run(debug=True)
