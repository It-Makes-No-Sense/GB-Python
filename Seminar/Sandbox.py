

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров')
        for k, v in sp.items():
            print(k, v)


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
            sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
    if command == '/add.number':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакта не существует!')
        else:
            phone = input('Введите номер: ')
            if phone in sp[name]['номер телефона']:
                print('Номер существует')
            else:
                sp[name]['номер телефона'].append(phone)
