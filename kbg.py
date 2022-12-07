from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/calculate')
def start():
    return render_template('calculate.html')

if __name__ == '__main__':
    app.run(debug=True)

