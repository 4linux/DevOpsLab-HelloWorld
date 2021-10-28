from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cappuccino")
def cappuccino():
    return render_template('cappuccino.py')

if __name__ == '__main__':
    app.run(debug=True)