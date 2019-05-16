from flask import Flask, render_template, request, escape, session, copy_current_request_context
import requests
import threading
import os
import git
from answers import equal

app: Flask = Flask(__name__)  # Test


@app.route('/')
@app.route('/0')
def q0():
    if 'answers' not in session:
        session['answers'] = 0
    return render_template('question.html',
                           next=1,
                           question='По какому произведению Вы проходите викторину? Кто автор произведения? $ echo Test2 > /dev/null/',
                           hints=[
                               'Название произведения',
                               'Автор'
                           ])


@app.route('/1', methods=['POST'])
def q1():
    if equal(request.form['Название произведения'], "ревизор"):
        session['answers'] += 1
    if equal(request.form['Автор'], "николай васильевич гоголь", "н. в. гоголь", "николай васильевич", "гоголь"):
        session['answers'] += 1
    return render_template('question.html',
                           next=2,
                           question='Чем берёт взятки судья?',
                           hints=[
                               'Чем?'
                           ])


@app.route('/2', methods=['POST'])
def q2():
    if equal(request.form['Чем?'], "борзый щенок"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=3,
                           question='Как зовут Бобчинского?',
                           hints=[
                               'Имя'
                           ])


@app.route('/3', methods=['POST'])
def q3():
    if equal(request.form['Имя'], "петр", "петр иванович"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=4,
                           question='''В тексте "Ревизора" дважды упоминается одна французская опера в пяти актах, поставленная в 1831 году. Первый раз Хлестаков во втором действии насвистывает что-то из неё, потом он же утверждает, что именно он является автором романа, лёгшего в основу либретто этой оперы. Назовите её.''',
                           hints=[
                               'Название оперы'
                           ])


@app.route('/4', methods=['POST'])
def q4():
    if equal(request.form['Название оперы'], "роберт", "роберт-дьявол"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=5,
                           question='У кого квартальный стянул всю штуку сукна?',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/5', methods=['POST'])
def q5():
    if equal(request.form['Фамилия'], "черняев", "у черняев"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=6,
                           question='Вставьте пропущенные слова в реплику городничего: "Я раз слушал его: ну, покамест говорил об ... и ...- ещё ничего, а как добрался до Александра Македонского, то я не могу вам сказать, что с ним сделалось"',
                           hints=[
                               'Первый пропуск',
                               'Второй пропуск'
                           ])


@app.route('/6', methods=['POST'])
def q6():
    if equal(request.form['Первый пропуск'], "ассирянин"):
        session['answers'] += 1
    if equal(request.form['Второй пропуск'], "вавилонянин"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=7,
                           question='Назовите фамилию купца, который не прислал городничему новую шпагу.',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/7', methods=['POST'])
def q7():
    if equal(request.form['Фамилия'], "абдулов"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=8,
                           question='Сколько Хлестаков взял в долг у Луки Лукича?',
                           hints=[
                               'Сумма'
                           ])


@app.route('/8', methods=['POST'])
def q8():
    if equal(request.form['Сумма'], "300", "300 рубль", "триста", "триста рубль"):
        session['answers'] += 1

    return render_template('question.html',
                           next=9,
                           question='Кем работает Ляпкин-Тяпкин?',
                           hints=[
                               'Профессия'
                           ])


@app.route('/9', methods=['POST'])
def q9():
    if equal(request.form['Профессия'], "судья"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=10,
                           question='Кто из чиновников или помещиков многодетный? Сколько у него детей?',
                           hints=[
                               'Имя',
                               'Количество детей'
                           ])


@app.route('/10', methods=['POST'])
def q10():
    if equal(request.form['Имя'], "артемий", "артемий филиппович", "земляника", "артемий филиппович земляника"):
        session['answers'] += 1
    if equal(request.form['Количество детей'], "5", "пять"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=11,
                           question='Кто среди чиновников является доносчиком?',
                           hints=[
                               'Имя'
                           ])


@app.route('/11', methods=['POST'])
def q11():
    if equal(request.form['Имя'], "артемий", "артемий филиппович", "земляника", "артемий филиппович земляника"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=12,
                           question='Назовите грехи городничего.\n(Двух хватит)',
                           hints=[
                               'Первый',
                               'Второй'
                           ])


@app.route('/12', methods=['POST'])
def q12():
    if equal(request.form['Первый'], "взяточничество", "приём взятка", "взятие взятка", "он брать взятка", "взяточник", "он взяточник", "коррупция"):
        session['answers'] += 1
    if equal(request.form['Второй'], "взяточничество", "приём взятка", "взятие взятка", "он брать взятка", "взяточник", "он взяточник", "коррупция"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=13,
                           question='Назовите фамилию Луки Лукича.',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/13', methods=['POST'])
def q13():
    if equal(request.form['Фамилия'], "шпекин"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=14,
                           question='Назовите чин Луки Лукича\n(Подсказка: чин - это не профессия).',
                           hints=[
                               'Чин'
                           ])


@app.route('/14', methods=['POST'])
def q14():
    if equal(request.form['Чин'], "титулярный советник"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=15,
                           question='Вставьте пропущенное название цвета в фразу Марьи Антоновны:\n"Ах, маменька, Вам нейдёт ...".',
                           hints=[
                               'Цвет'
                           ])


@app.route('/15', methods=['POST'])
def q15():
    if equal(request.form['Цвет'], "палевое"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=16,
                           question='А какая фамилия у Марьи Антоновны?',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/16', methods=['POST'])
def q16():
    if equal(request.form['Фамилия'], "сквозник-дмухановский"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=17,
                           question='Когда Бобчинский, рассказывая о первой встресе с Хлестаковым, говорит о том,что он встретился с Петром Ивановичем, Добчинский его перебивает и называет точное место встречи - это будка. А что в ней продавалось?',
                           hints=[
                               'Товар'
                           ])


@app.route('/17', methods=['POST'])
def q17():
    if equal(request.form['Товар'], "пирог"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=18,
                           question='Какую рыбу ели Петры Ивановичи в трактире, в котором жил Хлестаков в начале комедии.',
                           hints=[
                               'Название рыбы'
                           ])


@app.route('/18', methods=['POST'])
def q18():
    if equal(request.form['Название рыбы'], "семга"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=19,
                           question='Как звали трактирщика?',
                           hints=[
                               'Имя'
                           ])


@app.route('/19', methods=['POST'])
def q19():
    if equal(request.form['Имя'], "стас"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=20,
                           question='В день какого выдуманного Гоголем святого в город приехал Хлестаков?',
                           hints=[
                               'Имя'
                           ])


@app.route('/20', methods=['POST'])
def q20():
    if equal(request.form['Имя'], "василий египтянин", "василий"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=21,
                           question='Во сколько рублей обходится арбуз на балах Хлестакова?\n(По словам самого Хлестакова)',
                           hints=[
                               'Цена'
                           ])


@app.route('/21', methods=['POST'])
def q21():
    if equal(request.form['Цена'], "700", "700 рубль", "семьсот", "семьсот рубль"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=22,
                           question='Что, кроме супа, принесли Хлестакову в трактире, когда обещали, что это будет последний обед, пока он не заплатит?',
                           hints=[
                               'Название блюда'
                           ])


@app.route('/22', methods=['POST'])
def q22():
    if equal(request.form['Название блюда'], "жаркое"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=23,
                           question='Кто в немой сцене стоит "посередине, в виде столба, с распростертыми руками и запрокинутой назад головою"?',
                           hints=[
                               'Кто?'
                           ])


@app.route('/23', methods=['POST'])
def q23():
    if equal(request.form['Кто?'], "городничий", "антон антонович", "сквозник-дмухановский", "антон антонович сквозник-дмухановский"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=24,
                           question='По мнению Земляники смотритель училища хуже, чем ...',
                           hints=[
                               'Кто?'
                           ])


@app.route('/24', methods=['POST'])
def q24():
    if equal(request.form['Кто?'], "якобинец"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=25,
                           question='Кто сказал: "Я прошу вас покорнейше, как поедете в Петербург, скажите всем там вельможам разным: сенаторам и адмиралам, что вот, живет в таком-то городе .... Так и скажите: живет ...."',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/25', methods=['POST'])
def q25():
    if equal(request.form['Фамилия'], "бобчинский"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=26,
                           question='Именное повеление - чье?',
                           hints=[
                               'Чье?'
                           ])


@app.route('/26', methods=['POST'])
def q26():
    if equal(request.form['Чье?'], "император"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=27,
                           question='Куда Хлестаков написал письмо Тряпичкину?',
                           hints=[
                               'Место'
                           ])


@app.route('/27', methods=['POST'])
def q27():
    if equal(request.form['Место'], "почтамтский", "в почтамтский", "на почтамтский"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=28,
                           question='Возможный прообраз Хлестакова.',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/28', methods=['POST'])
def q28():
    if equal(request.form['Фамилия'], "пушкин", "свиньин"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=29,
                           question='Кто сказал "Так уж сделайте такую милость, ваше сиятельство. Если уже вы, то есть, не поможете в нашей просьбе, то уж не знаем, как и быть: просто хоть в петлю полезай"',
                           hints=[
                               'Профессия'
                           ])


@app.route('/29', methods=['POST'])
def q29():
    if equal(request.form['Профессия'], "купцы"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=30,
                           question='Из какого города едет Хлестаков? В какой?',
                           hints=[
                               'Откуда?',
                               'Куда?'
                           ])


@app.route('/30', methods=['POST'])
def q30():
    if equal(request.form['Откуда?'], "петербург", "из петербург", "из санкт-петербург", "санкт-петербург"):
        session['answers'] += 1
    if equal(request.form['Куда?'], "саратовская губерния", "в саратовская губерния", "в подкатиловка", "подкатиловка"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=31,
                           question='Сам не подозревая того, своим враньем Хлестаков выдал себя за...',
                           hints=[
                               'Чин'
                           ])


@app.route('/31', methods=['POST'])
def q31():
    if equal(request.form['Чин'], "разведчик", "за разведчик"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=32,
                           question='Городничий и Хлестаков говорят об одном и том же при их первой встрече?',
                           hints=[
                               'Да/нет'
                           ])


@app.route('/32', methods=['POST'])
def q32():
    if equal(request.form['Да/нет'], "да"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=33,
                           question='Кто из чиновников является масоном?',
                           hints=[
                               'Фамилия'
                           ])


@app.route('/33', methods=['POST'])
def q33():
    if equal(request.form['Фамилия'], "ляпкин-тяпкин"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=34,
                           question='Хлестаков получил взаймы больше ... рублей',
                           hints=[
                               'Сумма'
                           ])


@app.route('/34', methods=['POST'])
def q34():
    if equal(request.form['Сумма'], "1000", "1000 рублей", "тысяча", "тысяча рублей"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next=35,
                           question='Скольких губернаторов обманул городничий?',
                           hints=[
                               'Число'
                           ])


@app.route('/35', methods=['POST'])
def q35():
    if equal(request.form['Число'], "3", "три"):
        session['answers'] += 1
    print(session['answers'])

    return render_template('question.html',
                           next='results',
                           question='Сколько лет провел на службе Антон Антонович',
                           hints=[
                                'Число'
                           ])


@app.route('/results', methods=['POST'])
def results():
    if equal(request.form['Число'], "30", "тридцать", "тридцать лет", "30 лет"):
        session['answers'] += 1
    score = session['answers']
    session['answers'] = 0

    return render_template('results.html',
                           right=score,
                           all=40,
                           comment='')


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    GitHub listener webhook
    """
    if request.method == 'POST':
        repo = git.Repo('./mysite')
        origin = repo.remotes.origin
        repo.create_head('master',
                         origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()  # Test
        t = threading.Thread(target=reload)
        t.start()
        return '', 200
    else:
        return '', 400


def reload():
    r: requests.Response = requests.post(
        'https://pythonanywhere.com/api/v0/user/MrChAIKofE/webapps/MrChAIKofE.pythonanywhere.com/reload/', headers={'Authorization': f'Token {os.getenv("API_TOKEN")}', })
    req: requests.Request = r.request
    requests.post('https://canary.discordapp.com/api/webhooks/568151336034762772/86s8EnCQFc5UbtqV9bJacBligkFLM6CrgJhlPwTxYHmi2C3oPFRh5Ifpi_jgLgVnOkdo', data={'content': f'{r.status_code} {r.text} {req.headers} {req.data} {req.url}'})


@app.route('/version')
def get_version():
    '''
    Gets hash of last commit
    '''
    return git.Repo('./mysite').head.commit.hexsha


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
