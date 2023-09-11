import json
import os

sp = {'дядя коля': {'phones': ['8-800-555-35-35', '8-900-536-35-35'], 'city': 'Сыктыфкар', 'status': 'дядя'},
      'нюрка': {'phones': ['8-555-549-34-35'], 'city': 'Сыктыфкар', 'status': 'тетя'}}


def import_phonebook(phonebook):
    path = input('Введите путь к файлу.\n'
                 'Введите /exit для отмены импорта.\n'
                 'Пример: D:\GeekBrains\Python\Homework8\test.json')
    while True:
        if os.path.exists(path):
            with open(fr'{path}') as json_file:
                data = json.load(json_file)
            print('Словарь был загружен')
            break
        elif path == '/exit':
            return phonebook
        else:
            print('Что-то не так с путем. Попробуйте еще раз.')
    return data


def save(phonebook, filename):
    with open(f"{filename}.json", 'w') as file:
        json.dump(phonebook, file)
    print('Словарь сохранен')


while True:
    command = input('\nВведите /help для получения помощи\nВведите команду: ')
    if command == '/all':
        print('Вот текущий список номеров')
        for k, v in sp.items():
            print(k, v)
    elif command == '/help':
        print('\nСписок команд:\n'
              '/all - Вывести все контакты.\n'
              '/add.contact- Добавить новый контакт в справочник\n'
              '/edit - Изменить данные у контакта\n'
              '/save - Сохранить справочник\n'
              '/search - Поиск по справочнику\n'
              '/import - Импорт справочника\n'
              '/delete - Удаление контакта\n')
    elif command == '/add.contact':
        name = input('Введите имя нового контакта: ')
        if name in sp:
            print('Контакт существует!')
        else:
            coll = int(input('Сколько номеров вы хотите ввести: '))
            numbers = []
            for i in range(coll):
                number = input(f'Введите {i + 1} номер: ')
                numbers.append(number)
            city = input('Введите название города: ')
            status = input('Введите статус: ')
            sp[name] = {'phones': numbers, 'city': city, 'status': status}
    elif command == '/edit':
        name = input(f'{sp.keys()} \n Введите имя контакта в котором хотите сделать изменения: ')
        if name not in sp:
            print('Контакта не существует!')
        else:
            key = input(f'{sp[name].keys()}\n Введите что вы хотите изменить.\nЕсли несколько полей то через ","')
            if 'city' in str(key):
                city = input('Введите новое название города: ')
                sp[name]['city'] = city
                print('Город был изменен.')
            if 'phones' in str(key):
                add = input('Что вы хотите сделать с номером(ами)?\n'
                            '1 - Добавить новый\n'
                            '2 - Заменить номер\n'
                            '3 - Удалить номер')
                if add == '1':
                    phone = input('Введите новый номер: ')
                    if phone in sp[name]['phones']:
                        print('Номер существует')
                    else:
                        sp[name]['phones'].append(phone)
                elif add == '2':
                    phones_list = tuple(enumerate(sp[name]['phones']))
                    for i, y in phones_list:
                        print(i, '-', y)
                    number = int(input('Введите индентификатор номера который хотите заменить'))
                    phone = input('Введите новый номер: ')
                    if phone in sp[name]['phones']:
                        print('Номер существует')
                    else:
                        sp[name]['phones'][number] = phone
                        print(f'Новый номер {phone} был успешно добавлен.')
                elif add == '3':
                    phones_list = tuple(enumerate(sp[name]['phones']))
                    for i, y in phones_list:
                        print(i, '-', y)
                    number = int(input('Введите индентификатор номера который хотите удалить'))
                    sp[name]['phones'].pop(number)
            if 'status' in str(key):
                status = input('Введите новое название статуса: ')
                sp[name]['status'] = status
                print('Статус был изменен.')
    elif command == '/save':
        filename = input('Введите название вашего телефонного справочника')
        save(sp, filename)
    elif command == '/search':
        search = input('Поиск')
        search_res = []
        for k, v in sp.items():
            contact_info = k + ' ' + str(v)
            if search.lower() in contact_info.lower():
                search_res.append(k + ' ' + str(v))
        if len(search_res) > 0:
            print('Вот что я нашел по вашему запросу:')
            for i in search_res:
                print(i)
        else:
            print('Ничего не нашлось..')
    elif command == '/delete':
        name = input(f'{sp.keys()} \n Введите имя контакта в котором хотите сделать изменения: ')
        if name not in sp:
            print('Контакта не существует!')
        else:
            sp.pop(name)
            print(f'Контакт "{name}" был удален из справочника')
    elif command == '/import':
        sp = import_phonebook(sp)
    else:
        print('\nТакой команды нет!')
