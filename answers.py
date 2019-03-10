import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def NormalAnswer(answer) -> str:
    answer = answer.replace('"', '')
    answers = answer.split()
    answers = [morph.parse(i)[0].normal_form for i in answers]
    answer = ' '.join(answers)
    answer = answer.replace('ё', 'е')
    return(answer)


def equal(answer: str, *right_answers) -> bool:
    return answer in right_answers


def ScoresCount(questions) -> int:
    scores = 0
    for j in questions:
        for i in questions[j].values():
            i = NormalAnswer(i)
    if equal(questions[0]['Название произведения'], "ревизор"):
        scores += 1
    if equal(questions[0]['Автор'], "николай васильевич гоголь", "н. в. гоголь", "николай васильевич", "гоголь"):
        scores += 1
    if equal(questions[1]['Чем?'], "борзый щенок"):
        scores += 1
    if equal(questions[2]['Имя'], "петр", "петр иванович"):
        scores += 1
    if equal(questions[3]['Название оперы'], "роберт", "роберт-дьявол"):
        scores += 1
    if equal(questions[4]['Фамилия'], "черняев"):
        scores += 1
    if equal(questions[5]['Первый пропуск'], "ассирянин"):
        scores += 1
    if equal(questions[5]['Второй пропуск'], "вавилонянин"):
        scores += 1
    if equal(questions[6]['Фамилия'], "абдулов"):
        scores += 1
    if equal(questions[7]['Сумма'], "300", "300 рубль", "триста", "триста рубль"):
        scores += 1
    if equal(questions[8]['Профессия'], "судья"):
        scores += 1
    if equal(questions[9]['Имя'], "артемий", "артемий филиппович", "земляника", "артемий филиппович земляника"):
        scores += 1
    if equal(questions[9]['Количество детей'], "5", "пять"):
        scores += 1
    if equal(questions[10]['Имя'], "артемий", "артемий филиппович", "земляника", "артемий филиппович земляника"):
        scores += 1
    if equal(questions[11]['Первый'], "взяточничество", "приём взятка", "взятие взятка", "он брать взятка", "взяточник", "он взяточник", "коррупция"):
        scores += 1
    if equal(questions[11]['Второй'], "взяточничество", "приём взятка", "взятие взятка", "он брать взятка", "взяточник", "он взяточник", "коррупция"):
        scores += 1
    if equal(questions[12]['Фамилия'], "шпекин"):
        scores += 1
    if equal(questions[13]['Чин'], "титулярный советник"):
        scores += 1
    if equal(questions[14]['Цвет'], "палевое"):
        scores += 1
    if equal(questions[15]['Фамилия'], "сквозник-дмухановский"):
        scores += 1
    if equal(questions[16]['Товар'], "пирог"):
        scores += 1
    if equal(questions[17]['Название рыбы'], "семга"):
        scores += 1
    if equal(questions[18]['Имя'], "стас"):
        scores += 1
    if equal(questions[19]['Имя'], "василий египтянин"):
        scores += 1
    if equal(questions[20]['Цена'], "700", "700 рубль", "семьсот", "семьсот рубль"):
        scores += 1
    if equal(questions[21]['Название блюда'], "жаркое"):
        scores += 1
    if equal(questions[22]['Кто?'], "городничий", "антон антонович", "сквозник-дмухановский", "антон антонович сквозник-дмухановский"):
        scores += 1
    if equal(questions[23]['Кто?'], "якобинец"):
        scores += 1
    if equal(questions[24]['Фамилия'], "бобчинский"):
        scores += 1
    if equal(questions[25]['Чье?'], "император"):
        scores += 1
    if equal(questions[26]['Место'], "почтамтский", "в почтамтский", "на почтамтский"):
        scores += 1
    if equal(questions[27]['Фамилия'], "пушкин", "свиньин"):
        scores += 1
    if equal(questions[28]['Профессия'], "купцы"):
        scores += 1
    if equal(questions[29]['Откуда?'], "петербург", "из петербург", "из санкт-петербург", "санкт-петербург"):
        scores += 1
    if equal(questions[29]['Куда?'], "саратовская губерния", "в саратовская губерния", "в подкатиловка", "подкатиловка"):
        scores += 1
    if equal(questions[30]['Чин'], "разведчик", "за разведчик"):
        scores += 1
    if equal(questions[31]['Да/нет'], "да"):
        scores += 1
    if equal(questions[32]['Фамилия'], "ляпкин-тяпкин"):
        scores += 1
    if equal(questions[33]['Сумма'], "1000", "1000 рублей", "тысяча", "тысяча рублей"):
        scores += 1
    if equal(questions[34]['Число'], "3", "три"):
        scores += 1
    if equal(questions[35]['Число'], "30", "тридцать", "тридцать лет", "30 лет"):
        scores += 1
    return scores
