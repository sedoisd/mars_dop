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


@app.route('/list_prof/<list_mode>')
def list_prof(list_mode):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                   'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
                   'пилот дронов']
    return render_template('profession.html', mode=list_mode, professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {'title': 'Авто-форма',
             'surname': 'Watny',
             'name': 'Mark',
             'education': 'Высшее',
             'profession': 'Штурман',
             'sex': 'male',
             'motivation': 'Мечта застрять на Марсе',
             'ready': 'True'
             }
    return render_template('auto_answer.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
