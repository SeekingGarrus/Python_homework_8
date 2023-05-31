# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def showphon():
    with open('phon.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def newphon():
    with open('phon.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    

def findphon():
    with open('phon.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Кого ищем?: ')
        for i in book:
            if temp in i:
                print(i)

def delete_person(name):
    persons = read_data()
    with open("phon.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    persons = read_data()
    with open("phon.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Выберите режим работы справочника' + '\n'+'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(showphon())
    elif mode == '0':
        findphon()
    elif mode == '2':
        newphon()
    elif mode == '3':
        name = input('Кого удаляем?: ')
        delete_person()
    elif mode == '4':
        old_name = input('Имя, которого хотим переименовать?: ')
        new_name = input('Новые данные?: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('No mode')

# другой способ

def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as phon:
        for line in phon:
            print(*line.split(';'), end='')

def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as phon:
            for line in phon:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as phon:
        for line in phon:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as phon:
       phon.write(replaced)

def find_char():
    print('Выберите характеристику:')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'

def check_id_record(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_records(path, *find_char())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    return confirm

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите фамилию, имя, отчество, номер телефона через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'удалить')
    if record_id != 'q':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')


path = 'phon.txt'

try:                        
    file = open(path, 'r')  # открыть файл
except IOError:             # если нет файла он создается
    print('Создан новый справочник -> phon_book.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'список',
           '2': 'поиск',
           '3': 'изменение',
           '4': 'удаление',
           'q': 'выход'}

action = None
while action != 'q':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            print_records(path)
        elif action == '2':
            find_records(path, *find_char())
        elif action == '3':
            change_records(path)
        elif action == '4':
            delete_records(path)