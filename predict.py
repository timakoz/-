import random
print ('Привет, меня зовут Лоррейн Уоррен')
otvet = input('Давай погадаем? да или нет: ')
if otvet == 'да' or otvet == 'нет':
    if otvet == 'нет':
        print ('Ну что ты стешняешся, давай все равно погадаем')
else:
    print ('Не говори ерунду, давай все равно погадаем')
konechnyspisok = []
slovo = 0
spisok = ['Енот','Слон','Вор','Ковер','Мышеловка','Работа','Зубочистка']
colichestvoslov = len(spisok)
print ('Смотри, у меня есть', colichestvoslov, 'слов')
vyvodimslov = int(input('Введи количество слов из моего запаса и эти слова предскажут твою судьбу '))
if vyvodimslov > colichestvoslov or vyvodimslov <= 0:
    while vyvodimslov > colichestvoslov or vyvodimslov <= 0:
        print ('Ну, дорогой, такое количество слов не подходит')
        vyvodimslov = int(input('Введи количество слов из моего запаса и эти слова предскажут твою судьбу '))
kolichestvovkonechnomspiske = len(konechnyspisok)
while vyvodimslov != kolichestvovkonechnomspiske:
    randomslovo = random.randint(0,colichestvoslov - 1)
    slovo = spisok.pop(randomslovo)
    colichestvoslov = len(spisok)
    konechnyspisok.append(slovo)
    kolichestvovkonechnomspiske = len(konechnyspisok)
print ('Вот твоя судьба: ',*konechnyspisok)