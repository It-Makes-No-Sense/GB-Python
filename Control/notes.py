# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.
import time
import json


def note_list():
    global revers
    cnt = len(notes.keys())
    print(f'Кол-во заметок: {cnt}')
    list_d = list(notes.items())
    list_d.sort(key=lambda x: x[1][3], reverse=revers)
    if cnt > 0:
        for i, j in list_d:
            print(f'{i}, Name:{j[0]}, Create:{j[2]}, LastUpdate:{j[3]}')


def note_show(index):
    note = notes[index]
    print(f"""
    Индентификатор: {index}
    Название: {note[0]}
    Тело: {note[1]}
    Дата создания: {note[2]}
    Дата обновления: {note[3]}
    """)


def note_update(index):
    note = notes[index]
    while True:
        note_show(index)
        choice_upd = int(input("""
        1 - Чтобы изменить название заметки.
        2 - Чтобы изменить тело заметки.
        3 - Покинуть режим редактирования."""))
        if choice_upd == 1:
            name = input('Введите новое название.').strip()
            if len(name) > 0:
                note[0] = name
                note[3] = time.strftime("%d-%m-%Y %H:%M:%S")
                notes[index] = note
            else:
                print('Имя файла не может быть пустым!')
        elif choice_upd == 2:
            body = input('Введите новое тело.').strip()
            note[1] = body
            note[3] = time.strftime("%d-%m-%Y %H:%M:%S")
            notes[index] = note
        elif choice_upd == 3:
            break
        else:
            print('Такого № в меню нет!')


def note_open():
    try:
        with open('notes.json', 'r') as f:
            return json.load(f)
    except:
        return {}


def note_delete(index):
    if notes.get(index):
        notes.pop(index)
        print(f'Заметка c индексом {index} была успешно удалена.')
    else:
        print('Заметки с таким индентификатором не существует!')


def note_create(name):
    if len(notes.keys()) == 0:
        num = 0
    else:
        num = max(notes.keys())
    notes[num + 1] = [name, 'Empty', time.strftime("%d-%m-%Y %H:%M:%S"),
                      time.strftime("%d-%m-%Y %H:%M:%S")]
    print(f'Заметка {name} была успешно создана! Её идентификатор {max(notes.keys())}')


def note_save():
    with open('notes.json', 'w') as f:
        json.dump(notes, f)
        print('Notes was saved!')


def check_input(text):
    if ' ' in text:
        res = text.split(' ', 1)[1]
        if res == '':
            return None
        else:
            return res
    else:
        return None


def choices(choice=None):
    global revers
    modif = check_input(choice)
    if choice == '/help':
        print("""
        /sort - Поменять сортировку по времени.
        /list - Показать список всех заметок.
        /create NAME - Создать новую заметку, где NAME, её название.
        /delete N - Удалить заметку, где N - её уникальный номер.
        /update N - Редактировать заметку, где N - её уникальный номер.
        /show N - Показать заметку, где N - её уникальный номер.
        /save - Сохранить изменения.
        /quit - Закрыть программу. (Изменения не сохраняются, если перед командой не выполнить /save !)
        """)
    elif choice == '/list':
        note_list()
    elif choice == '/sort':
        revers = not revers
    elif '/create' in choice:
        if modif:
            note_create(modif)
        else:
            print('Вы не ввели имя заметки!')
    elif '/delete' in choice:
        if modif:
            note_delete(modif)
        else:
            print('Вы не ввели номер заметки!')
    elif '/update' in choice:
        if modif:
            note_update(modif)
        else:
            print('Вы не ввели номер заметки!')
    elif '/show' in choice:
        if modif:
            note_show(modif)
        else:
            print('Вы не ввели номер заметки!')
    elif choice == '/save':
        note_save()
    elif choice == '/quit':
        print('Всего хорошего!')
        quit()
    else:
        print('Данной команды не существует.')


revers = True
notes = note_open()

while True:
    print('\nВведите /help для вывода списка команд.')
    try:
        choices(input("Введите команду:").strip())
    except ValueError as e:
        print("Ошибка при передаче значения, указан не тот тип данных.")
