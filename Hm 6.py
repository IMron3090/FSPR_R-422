"""
Изменяемые 
    set - множество 
    dict - словарь 
    list - список 
 
Неизменяемые 
    bin 
    frozenset - множество 
    tuple - кортеж 
    int 
    float 
    str 
    bool 
    None

"""
# INDEX

# Метод возвращает позицию при первом вхождении указанного значения.index()
pens = [22, 35, 680, 902, 920, 300]

x = pens.index(300)

print(x)

# COUNT

# Метод возвращает количество элементов с заданным значением.count()

phones = [4, 1, 9, 2, 8, 7, 3, 9, 1]

b = phones.count(9)

print(b)