from flask import Flask, render_template, request, escape, session, copy_current_request_context
import random

app: Flask = Flask(__name__)

def check_answers(answers):
    return random.randint(0, len(answers) + 1)

@app.route('/')
@app.route('/0')
def q0():
    if 'answers' not in session:
        session['answers'] = []
    return render_template('question.html',
                            next=1,
                            question='По какому произведению Вы проходите викторину? Кто автор произведения?',
                            hints=[
                                'Название произведения',
                                'Автор'
                            ])

@app.route('/1', methods=['POST'])
def q1():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=2,
                            question='Чем берёт взятки судья?',
                            hints=[
                                'Чем?'
                            ])

@app.route('/2', methods=['POST'])
def q2():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=3,
                            question='Как зовут Бобчинского?',
                            hints=[
                                'Имя'
                            ])

@app.route('/3', methods=['POST'])
def q3():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=4,
                            question='''В тексте "Ревизора" дважды упоминается одна французская опера в пяти актах, поставленная в 1831 году. Первый раз Хлестаков во втором действии насвистывает что-то из неё, потом он же утверждает, что именно он является автором романа, лёгшего в основу либретто этой оперы. Назовите её.''',
                            hints=[
                                'Название оперы'
                            ])

@app.route('/4', methods=['POST'])
def q4():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=5,
                            question='У кого квартальный стянул всю штуку сукна?',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/5', methods=['POST'])
def q5():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=6,
                            question='Вставьте пропущенные слова в реплику городничего: "Я раз слушал его: ну, покамест говорил об ... и ...- ещё ничего, а как добрался до Александра Македонского, то я не могу вам сказать, что с ним сделалось"',
                            hints=[
                                'Первый пропуск',
                                'Второй пропуск'
                            ])

@app.route('/6', methods=['POST'])
def q6():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=7,
                            question='Назовите фамилию купца, который не прислал городничему новую шпагу.',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/7', methods=['POST'])
def q7():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=8,
                            question='Сколько Хлестаков взял в долг у Луки Лукича?',
                            hints=[
                                'Сумма'
                            ])

@app.route('/8', methods=['POST'])
def q8():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=9,
                            question='Кем работает Ляпкин-Тяпкин?',
                            hints=[
                                'Профессия'
                            ])

@app.route('/9', methods=['POST'])
def q9():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=10,
                            question='Кто из чиновников или помещиков многодетный? Сколько у него детей?',
                            hints=[
                                'Имя',
                                'Количество детей'
                            ])

@app.route('/10', methods=['POST'])
def q10():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=11,
                            question='Кто среди чиновников является доносчиком?',
                            hints=[
                                'Имя'
                            ])

@app.route('/11', methods=['POST'])
def q11():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=12,
                            question='Назовите грехи городничего.\n(Двух хватит)',
                            hints=[
                                'Первый',
                                'Второй'
                            ])

@app.route('/12', methods=['POST'])
def q12():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=13,
                            question='Назовите фамилию Луки Лукича.',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/13', methods=['POST'])
def q13():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=14,
                            question='Назовите чин Луки Лукича\n(Подсказка: чин - это не профессия).',
                            hints=[
                                'Чин'
                            ])

@app.route('/14', methods=['POST'])
def q14():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=15,
                            question='Вставьте пропущенное название цвета в фразу Марьи Антоновны:\n"Ах, маменька, Вам нейдёт ...".',
                            hints=[
                                'Цвет'
                            ])

@app.route('/15', methods=['POST'])
def q15():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=16,
                            question='А какая фамилия у Марьи Ивановны?',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/16', methods=['POST'])
def q16():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=17,
                            question='Когда Бобчинский, рассказывая о первой встресе с Хлестаковым, говорит о том,что он встретился с Петром Ивановичем, Добчинский его перебивает и называет точное место встречи - это будка. А что в ней продавалось?',
                            hints=[
                                'Товар'
                            ])

@app.route('/17', methods=['POST'])
def q17():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=18,
                            question='Какую рыбу ели Петры Ивановичи в трактире, в котором жил Хлестаков в начале комедии.',
                            hints=[
                                'Название рыбы'
                            ])

@app.route('/18', methods=['POST'])
def q18():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=19,
                            question='Как звали трактирщика?',
                            hints=[
                                'Имя'
                            ])

@app.route('/19', methods=['POST'])
def q19():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=20,
                            question='В день какого выдуманного Гоголем святого в город приехал Хлестаков?',
                            hints=[
                                'Имя'
                            ])

@app.route('/20', methods=['POST'])
def q20():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=21,
                            question='Во сколько рублей обходится арбуз на балах Хлестакова?\n(По словам самого Хлестакова)',
                            hints=[
                                'Цена'
                            ])

@app.route('/21', methods=['POST'])
def q21():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=22,
                            question='Что, кроме супа, принесли Хлестакову в трактире, когда обещали, что это будет последний обед, пока он не заплатит?',
                            hints=[
                                'Название блюда'
                            ])

@app.route('/22', methods=['POST'])
def q22():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=23,
                            question='Кто в немой сцене стоит "посередине, в виде столба, с распростертыми руками и запрокинутой назад головою"?',
                            hints=[
                                'Кто?'
                            ])

@app.route('/23', methods=['POST'])
def q23():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=24,
                            question='По мнению Земляники смотритель училища хуже, чем ...',
                            hints=[
                                'Кто?'
                            ])

@app.route('/24', methods=['POST'])
def q24():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=25,
                            question='Кто сказал: "Я прошу вас покорнейше, как поедете в Петербург, скажите всем там вельможам разным: сенаторам и адмиралам, что вот, живет в таком-то городе .... Так и скажите: живет ...."',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/25', methods=['POST'])
def q25():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=26,
                            question='Именное повеление - чье?',
                            hints=[
                                'Чье?'
                            ])

@app.route('/26', methods=['POST'])
def q26():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=27,
                            question='Куда Хлестаков написал письмо Хлестакову?',
                            hints=[
                                'Место'
                            ])

@app.route('/27', methods=['POST'])
def q27():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=28,
                            question='Возможный прообраз Хлестакова.',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/28', methods=['POST'])
def q28():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=29,
                            question='Кто сказал "Так уж сделайте такую милость, ваше сиятельство. Если уже вы, то есть, не поможете в нашей просьбе, то уж не знаем, как и быть: просто хоть в петлю полезай"',
                            hints=[
                                'Профессия'
                            ])

@app.route('/29', methods=['POST'])
def q29():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=30,
                            question='Из какого города едет Хлестаков? В какой?',
                            hints=[
                                'Откуда',
                                'Куда'
                            ])

@app.route('/30', methods=['POST'])
def q30():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=31,
                            question='Сам не подозревая того, своим враньем Хлестаков выдал себя за...',
                            hints=[
                                'Чин'
                            ])

@app.route('/31', methods=['POST'])
def q31():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=32,
                            question='Городничий и Хлестаков говорят об одном и том же при их первой встрече?',
                            hints=[
                                'Да/нет'
                            ])

@app.route('/32', methods=['POST'])
def q32():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=33,
                            question='Кто из чиновников является масоном?',
                            hints=[
                                'Фамилия'
                            ])

@app.route('/33', methods=['POST'])
def q33():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=34,
                            question='Хлестаков получил взаймы больше ... рублей',
                            hints=[
                                'Сумма'
                            ])

@app.route('/34', methods=['POST'])
def q34():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next=35,
                            question='Скольких губернаторов обманул городничий?',
                            hints=[
                                'Число'
                            ])

@app.route('/35', methods=['POST'])
def q35():
    session['answers'].append(request.form)
    return render_template('question.html',
                            next='results',
                            question='Сколько лет провел на службе Антон Антонович',
                            hints=[
                                'Число'
                            ])

@app.route('/results', methods=['POST'])
def results():
    session['answers'].append(request.form)
    return render_template('results.html',
                            right=check_answers(session['answers']),
                            all=36,
                            comment='Чебурек')

app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
