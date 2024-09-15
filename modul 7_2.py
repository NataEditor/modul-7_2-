import io

from pprint import pprint

file_name = 'list_sring.txt'
info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']


def custom_write(file_name, strings):
    str_positions = { }
    file = open(file_name, 'a', encoding='utf-8')
    for i, j in enumerate(strings):
        kl = (i + 1, file.tell())
        str_positions[kl] = j
        file.write(j + '\n')
    file.close()
    return str_positions




result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

