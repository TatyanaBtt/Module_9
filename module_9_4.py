first = 'Мама мыла раму'
second = 'Рамена мало было'

letter_match = list(map(lambda x, y: x in y, first, second))
print(letter_match)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('text.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 258, {'key': 'value', 'key2': 'value2'})

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return(choice(self.words))

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Yes', 'No', 'Maybe')
print(first_ball())
print(first_ball())
print(first_ball())