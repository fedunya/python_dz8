def add(file_name, database_entry):
    with open(file_name, 'a', encoding = 'utf-8') as csvfile:
        wr_csv = csv.writer(csvfile, lineterminator = '\r')
        wr_csv.writerow(database_entry)                
    return 
def unload(file_name):
    fields = []
    data_base = []
    with open(file_name, 'r', encoding = 'utf-8') as f:
        csv_f = csv.reader(f)
        fields = next(csv_f)            
        for row in csv_f:            
            data_base.append(row)
        count_entrys = csv_f.line_num
    return data_base, fields, count_entrys
def upload(file_name, fields, data):
    with open(file_name, 'w', encoding = 'utf-8') as csvfile:
        wr_csv = csv.writer(csvfile, lineterminator = '\r')
        wr_csv.writerow(fields)
    with open(file_name, 'a', encoding = 'utf-8') as csvfile:
        wr_csv = csv.writer(csvfile, lineterminator = '\r')    
        for i in data:
            wr_csv.writerow(i)
    return
def find(data_base, value, index):
    res_find = []
    for line in data_base:
        if line[index-1] == value:
            res_find.append(line)
    return res_find
def delete(data_base, id):
    data_base.pop(int(id) - 1)
    print('Запись успешно удалена из базы.')
    j = 1
    for i in data_base:
        i[0] = j
        j+=1
    return data_base

import csv
