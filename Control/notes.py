# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.
from datetime import datetime
import json


def note_list():
    cnt = len(notes.keys())
    print(f'Кол-во заметок: {cnt}')
    if cnt > 0:
        for i, j in notes.items():
            print(f'{i}:{j[0]}')


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
        4 - Покинуть режим редактирования.
        """))
        if choice_upd == 1:
            name = input('Введите новое название.').strip()
            if len(name) > 0:
                note[0] = name
                notes[index] = note
            else:
                print('Имя файла не может быть пустым!')
        elif choice_upd == 2:
            body = input('Введите новое тело.').strip()
            note[1] = body
            notes[index] = note
        elif choice_upd == 3:
            break
        else:
            print('Такого № в меню нет!')
    note_save()


def note_open():
    pass


def note_delete(index):
    pass


def note_create(name):
    notes[max(notes.keys()) + 1] = [name, 'Empty', datetime.strftime("%d/%m/%Y %H:%M:%S"),
                                    datetime.strftime("%d/%m/%Y %H:%M:%S")]
    print(f'Заметка {name} была успешно создана! Её идентификатор {max(notes.keys())}')


def note_save():
    with open('notes.json', 'w') as f:
        json.dump(notes, f)


def check_input(text):
    if ' ' in text:
        res = text.split(' ')[1]
        if res == '':
            return None
        else:
            return res
    else:
        return None


def choices(choice=None):
    modif = check_input(choice)
    if choice == '/help':
        print("""
        /list - Показать список всех заметок.
        /create NAME - Создать новую заметку, где NAME, её название.
        /delete N - Удалить заметку, где N - её уникальный номер.
        /update N - Редактировать заметку, где N - её уникальный номер.
        /show N - Показать заметку, где N - её уникальный номер.
        """)
    elif choice == '/list':
        note_list()
    elif '/create' in choice:
        if modif:
            note_create(modif)
        else:
            print('Вы не ввели имя заметки!')
    elif '/delete' in choice:
        if modif:
            note_delete(int(modif))
        else:
            print('Вы не ввели номер заметки!')
    elif '/update' in choice:
        if modif:
            note_update(int(modif))
        else:
            print('Вы не ввели номер заметки!')
    elif '/show' in choice:
        if modif:
            note_show(int(modif))
        else:
            print('Вы не ввели номер заметки!')
    else:
        print('Данной команды не существует.')


try:
    with open('notes.json', 'r') as file:
        notes = json.load(file)
except:
    notes = {}

while True:
    print('Введите /help для вывода списка команд.')
    choices(input("Введите команду:").strip())
