TITLE = "Древняя библиотека"
STATEMENT_TEMPLATE = '''
Богатство этой библиотеки не сравнится с её неприступностью.
Восточные мудрецы когда-то называли её крепостью, составленной из книг. О ней ходили красивейшие легенды и писались трактаты.
А оставить свою книгу в этой библиотеке было честью для правителей со всего мира...

Сейчас всё это забыто, о библиотеке почти не вспоминают.
Единственное, что сохранилось до наших дней, — это система её защиты.

В библиотеке есть кое-что, что мы хотим получить. Просто сделайте это, и получите своё вознаграждение.

`nc secure-library.contest.qctf.ru 20003`

[library](/static/files/3rl6qrj3w2/library)
'''

def generate(context):
    return TaskStatement(TITLE, STATEMENT_TEMPLATE)
