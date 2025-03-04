from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def workout(prof):
    params = dict()
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        params['workout'] = 'Инженерные тренажеры'
        params['image'] = url_for('static', filename='image/spaceship_engineering.png')
    else:
        params['workout'] = 'Научные симуляторы'
        params['image'] = url_for('static', filename='image/spaceship_science.png')
    params['title'] = 'Расположение модулей для деятельности по профессиям'
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
