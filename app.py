from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', category='all')

@app.route('/<category_name>')
def category(category_name):
    return render_template('index.html', category=category_name)



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event_description = request.form['event']
        category = request.form['category']

        # Здесь можно сохранить заявку в файл, базу данных или отправить на email
        print(f"Заявка: {name}, {email}, {event_description}, категория: {category}")

        return redirect(url_for('thank_you'))

    return render_template('submit.html')


@app.route('/thank-you')
def thank_you():
    return '<h2>Спасибо за заявку! Мы скоро с вами свяжемся.</h2>'


@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/sport")
def sport():
    return render_template("sport.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route('/category/<category>')
def show_category(category):
    events = {
        'music': [
            {'title': 'Концерт на крыше', 'desc': '21 июля 2025 • Алматы', 'lat': 43.2389, 'lon': 76.8897},
            {'title': 'Jazz Night', 'desc': '25 июля 2025 • Нур-Султан', 'lat': 51.1605, 'lon': 71.4704},
        ],
        'education': [
            {'title': 'Мастер-класс по UI/UX', 'desc': '22 июля 2025 • Нур-Султан', 'lat': 51.1605, 'lon': 71.4704},
            {'title': 'Лекция по кибербезопасности', 'desc': '30 июля 2025 • Алматы', 'lat': 43.2389, 'lon': 76.8897},
        ],
        'sport': [
            {'title': 'Утренняя йога', 'desc': '23 июля 2025 • Караганда', 'lat': 49.8047, 'lon': 73.1094},
            {'title': 'Забег 5 км', 'desc': '28 июля 2025 • Шымкент', 'lat': 42.3417, 'lon': 69.5901},
        ],
        'art': [
            {'title': 'Выставка современного искусства', 'desc': '24 июля 2025 • Алматы', 'lat': 43.2389,
             'lon': 76.8897},
            {'title': 'Пленэр с художниками', 'desc': '27 июля 2025 • Нур-Султан', 'lat': 51.1605, 'lon': 71.4704},
        ]
    }

    selected_events = events.get(category, [])

    return render_template('category.html', category=category, events=selected_events)


events = [
    {
        'title': 'Йога в парке',
        'description': 'Утренняя йога в центре города.',
        'lat': 43.2389,
        'lon': 76.8897
    },
    ...
]


if __name__ == '__main__':
    app.run(debug=True)





