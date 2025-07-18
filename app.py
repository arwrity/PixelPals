from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', category='all')

@app.route('/<category_name>')
def category(category_name):
    return render_template('index.html', category=category_name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email and password:
            return redirect(url_for("home"))
        else:
            return "Invalid credentials", 401

    return render_template("login.html")



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event_description = request.form['event']
        category = request.form['category']

        print(f"Заявка: {name}, {email}, {event_description}, категория: {category}")

        return redirect(url_for('thank_you'))

    return render_template('submit.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route("/music")
def music():
    return render_template("music.html")


@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/sport")
def sport():
    return render_template("sport.html")


@app.route('/category/<category>')
def show_category(category):
    try:
        return render_template(f'category_{category}.html')
    except:
        return "<h2>Категория не найдена</h2>", 404


@app.route('/category_music')
def category_music():
    return render_template('category_music.html', title="Музыка")

@app.route('/category_education')
def category_education():
    return render_template('category_education.html', title="Образование")

@app.route('/category_sport')
def category_sport():
    return render_template('category_sport.html', title="Спорт")

@app.route('/category_art')
def category_art():
    return render_template('category_art.html', title="Искусство")


if __name__ == '__main__':
    app.run(debug=True)





