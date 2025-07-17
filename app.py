from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', category='all')

@app.route('/category/<string:name>')
def category(name):
    return render_template('home.html', category=name)

if __name__ == '__main__':
    app.run(debug=True)
