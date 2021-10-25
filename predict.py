import random
konechnyspisok = []
slovo = 0
spisok = ['Енот','Слон','Вор','Ковер','Мышеловка','Работа','Зубочистка']
colichestvoslov = len(spisok)
print ('Количество слов в массиве', colichestvoslov)
vyvodimslov = int(input('Введите количество слов '))
if vyvodimslov > colichestvoslov or vyvodimslov <= 0:
    while vyvodimslov > colichestvoslov or vyvodimslov <= 0:
        print ('error')
        vyvodimslov = int(input('Введите количество слов '))
kolichestvovkonechnomspiske = len(konechnyspisok)
while vyvodimslov != kolichestvovkonechnomspiske:
    randomslovo = random.randint(0,colichestvoslov - 1)
    slovo = spisok.pop(randomslovo)
    colichestvoslov = len(spisok)
    konechnyspisok.append(slovo)
    kolichestvovkonechnomspiske = len(konechnyspisok)
print (*konechnyspisok)