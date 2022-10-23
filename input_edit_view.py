def menu_item_input(msg_out, n):
    a = ['1','2','3','4','5','6']
    num = input(msg_out)
    while num not in a[:n]: num = input('Неверный ввод! Повторите: ')
    return int(num)
def input_entry(count_entrys):
    database_entry = [count_entrys]
    surname = input('Введите фамилию сотрудника: ')
    database_entry.append(surname)
    name = input('Введите имя сотрудника: ')
    database_entry.append(name)
    patronymic = input('Введите отчество сотрудника: ')
    database_entry.append(patronymic)
    phone = input('Введите телефон сотрудника: ')
    while len(phone) != 11 or not phone.isdigit():
        phone = input('Неверный ввод! Повторите: ')
    database_entry.append(phone)
    print('Статус сотрудника:\n1. Работает\n2. Отпуск\n3. Уволен')
    num = menu_item_input('Введите цифру статуса сотрудника: ', 3)
    if num == 1: status = 'Работает'
    elif num == 2: status = 'Отпуск'
    else: status = 'Уволен'
    database_entry.append(status)
    return database_entry
def view_horizontal(data, fields):
    for row in data:        
        print(f'{fields[0]}: {row[0]}, {fields[1]}: {row[1]}, '
            f'{fields[2]}: {row[2]}, {fields[3]}: {row[3]} '
            f'{fields[4]}: {row[4]}, {fields[5]}: {row[5]}')
    return
def view_vertical(data, fields):
    for row in data:        
        print(f'{fields[0]}: {row[0]}\n{fields[1]}: {row[1]}\n'
            f'{fields[2]}: {row[2]}\n{fields[3]}: {row[3]}\n'
            f'{fields[4]}: {row[4]}\n{fields[5]}: {row[5]}\n\n')
    return
def input_id(count):
    id = input('Введите id записи: ')
    while not id.isdigit():
        id = input('Неверный ввод! Повторите: ')
    while int(id) > count - 1:
        id = input('В базе нет записи с таким номером! Повторите: ')
    return id