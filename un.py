import os
import json
import random
from io import BytesIO
from sqlite3.dbapi2 import paramstyle

from PIL import Image
from flask import Flask, render_template, url_for, request
from classes import EmergencyAccess

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


@app.route('/emergency_access_login', methods=['GET', 'POST'])
def emergency_access_login():
    access = EmergencyAccess()
    if access.validate_on_submit():
        return 'Процесс аутентификации'
    return render_template('emergency_access.html', title='Авторизация в аварийный доступ', form=access)


@app.route('/distribution')
def distribution():
    staff_list = ['Ридли Скотт',
                  'Энди Уир',
                  'Марк Уотни',
                  'Венката Капур',
                  'Тедди Сандерс ',
                  'Шон Бин']
    return render_template('distribution.html', staff_list=staff_list)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    url_image = 'image/adult_mars.png'
    colors = {'female': {'child': '#ffa07a', 'adult': '#ff4500'}, 'male': {'child': '#b0c4de', 'adult': '#007ff0'}}
    if int(age) < 21:
        url_image = 'image/child_mars.png'
        color = colors[sex]['child']
    else:
        color = colors[sex]['adult']

    return render_template('table.html', url_image=url_for('static', filename=url_image),
                           color=color)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    landscape_path = os.path.join('static', 'image', 'landscapes')
    filenames = list(map(lambda x: os.path.join(landscape_path, x), os.listdir(landscape_path)))
    # print(filenames)
    if request.method == 'GET':
        return render_template('galery.html', filenames=filenames)
    elif request.method == 'POST':
        f = request.files.get('file')
        if f:
            data = f.read()
            im = Image.open(BytesIO(data))
            # im.show()
            n = len(os.listdir(landscape_path)) + 1
            im.save('static/image/landscapes/landsc_{n}.{im_format}'.format(im_format=im.format, n=n))
        landscape_path = os.path.join('static', 'image', 'landscapes')
        filenames = list(map(lambda x: os.path.join(landscape_path, x), os.listdir(landscape_path)))
        return render_template('galery.html', filenames=filenames)


@app.route('/member')
def member():
    with open('templates/members.json', encoding="utf-8") as file:
        json_data = json.load(file)
        my_dict = random.choices(json_data)[0]
        my_dict['image'] = os.path.join('static', 'image', 'avatars', my_dict['image'])
    return render_template('member.html', params=my_dict)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
