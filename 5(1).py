import csv

alph = sorted(' ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
d = {alph[i]: i + 1 for i in range(len(alph))}



def hassh(s):
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    i = 0
    for cash in s:
        hash_value += d[cash] * p ** i
        i += 1
    return int(hash_value % m)


with open('students.csv', encoding='utf-8') as file, open('students_with_cash.csv', 'w', encoding='utf-8', newline = '') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter = ',')

    res.writerow(data[0])
    for stroka in data[1:]:
        fio = stroka[1]
        h = hassh(fio)
        stroka[0] = h
        res.writerow(stroka)