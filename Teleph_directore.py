from pathlib import Path

file_path = Path('Telephone_book.txt')


def reading(name):
    print('Фамилия   Имя   Отчество   Телефон')
    with open(name, 'r', encoding='utf8') as text_file:
        for line in text_file:
            print(line.strip())


def add_data(name):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    with open(name, 'a', encoding='utf8') as text_file:
        text_file.write(f'\n{str_new1}, {str_new2}, {str_new3}, {str_new4}')


def search_item(name):
    item = input('Характеристика для поиска записи: ')
    with open(name, 'r', encoding='utf8') as text_file:
        for line in text_file:
            if item.lower() in line.lower():
                print(line.strip())


def search_item_2(name):
    item = input('Характеристика для поиска записи: ')
    item_type = int(input('Введите номер(0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Номер телефона: '))
    with open(name, 'r', encoding='utf8') as text_file:
        for line in text_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)



def sort_data(name):
    list_1 = []
    item_type = int(input('Введите параметр для сортировки (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(name, 'r', encoding='utf8') as text_file:
        for line in text_file:
            line = line.strip().split(', ')
            list_1.append(line)
        list_1.sort(key=lambda person: person[item_type])
    with open(name, 'w', encoding='utf8') as text_file:
        for line in list_1:
            line = ', '.join(line) + '\n'
            text_file.write(line)


def change_data(name):
    item = input('Что надо изменить? ')
    item_type = int(input('Введите номер(0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Номер телефона: '))
    item_new = input('Введите новое значение: ')
    with open(name, 'r', encoding='utf8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            line = line.strip().split(', ')
            if item.lower() in line[item_type].lower():
                with open(name, 'w', encoding='utf8') as text_file:
                    for line in lines:
                        line = line.strip().split(', ')
                        if item.lower() in line[item_type].lower():
                            line[item_type] = item_new
                        text_file.write(', '.join(line) + '\n')
    print(f'Запись — {item}, изменена на — {item_new}\n')


def del_data(name):
    item = input('Что удаляем? ')
    item_type = int(input('Введите номер(0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Номер телефона: '))
    with open(name, 'r', encoding='utf8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            line = line.strip().split(', ')
            if item.lower() in line[item_type].lower():
                with open(name, 'w', encoding='utf8') as text_file:
                    for line in lines:
                        line = line.strip().split(', ')
                        if item.lower() != line[item_type].lower():
                             text_file.write(', '.join(line) + '\n')


def main():
    print('Выберите одно из действий: ', 
          '1)Вывести информацию на экран',
          '2)Добавление новых контактов', 
          '3)Поиск по элементу во всем справочнике',
          '4)Поиск по Фамилии, Имени, Отчеству, Номеру телефона',
          '5)Сортировка данных в справочнике по выбранному параметру',
          '6)Изменение данных',
          '7)Удаление данных',
          '8)Выход из программы', sep='\n', end='\n')   
    match input('Действие: '):
        case '1':
            reading(file_path)
        case '2':
            add_data(file_path)
        case '3':
            search_item(file_path)
        case '4':
            search_item_2(file_path)
        case '5':
            sort_data(file_path)
        case '6':
            change_data(file_path)
        case '7':
            del_data(file_path)
        case '8':
            print('Good bye!')

            
main()
#add_data(file_path)
#reading(file_path)
#search_item(file_path)
#search_item_2(file_path)
#sort_data(file_path)
#change_data(file_path)
#del_data(file_path)
