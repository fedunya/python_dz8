def menu():
    os.system("cls")
    print('''
*************************************
*                                   *
*         БАЗА СОТРУДНИКОВ          *
*                                   *
*************************************
''')
    print('МЕНЮ:\n1. Добавление записи.\n2. Редактирование записи.\n'
        '3. Поиск записей.\n4. Удаление записи.\n'
        '5. Просмотр всей базы на экране.\n6. Выход из программы.')
    key = iev.menu_item_input('Введите номер выбранного пункта меню: ', 6)
    data_base, fields, count_entrys = md.unload('Base_employees.csv')
    if key == 1:
        database_entry = iev.input_entry(count_entrys)
        md.add('Base_employees.csv', database_entry)
        print('Запись успешно добавлена в базу.')
        input('Нажмите любую клавишу для продолжения.')
        menu()
    elif key == 2:
        id = iev.input_id(count_entrys)
        _ = []
        print('Редактируемая запись:')
        _.append(data_base[int(id) - 1])
        iev.view_horizontal(_, fields)
        db = iev.input_entry(int(id))
        data_base[int(id) - 1] = db
        md.upload('Base_employees.csv', fields, data_base)
        print('Запись успешно отредактирована и сохранена в базе.')
        input('Нажмите любую клавишу для продолжения.')
        menu()
    elif key == 3:
        print('По какому параметру будем проводить поиск:\n1. id\n2. Фамилия\n'
            '3. Имя\n4. Отчество\n5. Телефон\n6. Статус')
        index = iev.menu_item_input('Введите номер поля для поиска: ', 6)
        value = input('Введите параметр поиска: ')
        res_find = md.find(data_base, value, index)
        if res_find == []:
            print('По заданному параметру ничего не найдено')
        else: iev.view_horizontal(res_find, fields)
        input('Нажмите любую клавишу для продолжения.')
        menu()
    elif key == 4:
        id = iev.input_id(count_entrys)
        _ = []
        print('Удаляемая запись:')
        _.append(data_base[int(id) - 1])
        iev.view_horizontal(_, fields)
        answer = input('Для подтверждения удаления нажмите d: ')
        if answer == 'd':
            md.delete(data_base, id)
            md.upload('Base_employees.csv', fields, data_base)
        else: print('Вы передумали удалять запись.')        
        input('Нажмите любую клавишу для продолжения.')
        menu()
    elif key == 5:
        n = iev.menu_item_input('Выберите формат вывода телефонной книги на экран:\n'
                        '1. Горизонтальный - в одной строке один контакт.\n'
                        '2. Вертикальный - элементы контакта выводятся вертикально,'
                        ' разделитель - пустая строка.\n-> ', 2)
        if n == 1: iev.view_horizontal(data_base, fields)
        else: iev.view_vertical(data_base, fields)
        input('Нажмите любую клавишу для продолжения.')
        menu()
    else: print('Вы завершили работу программы. До свидания!')
    return


import os
import model as md
import input_edit_view as iev
