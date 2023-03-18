def bin1(x):
    a = bin(x)
    lst_bin_num = list(a)
    lst_bin_num.remove('b')
    lst_bin_num.remove(lst_bin_num[0])
    return_need = ''
    for d in lst_bin_num:
        return_need += d
    return return_need
def bin_dec(data):
    number = 0
    len_dat = len(data)
    for i in range(0, len_dat):
        number += int(data[i]) * (2**(len_dat - i -1))
    return number
print('Приветствую вас в шифровальной машине')
print('--------------------------------------------------------------------------------')
print('Выберите действие: ')
print('1 - шифровка')
print('2 - расшифровка')
print('0 - выход')
while True:
    try:
        vibor1 = input('Ваше действие: ')
        while True: 
            if vibor1 == '1' or vibor1 == '2' or vibor1 == '0':
                break
            print('Неверный ввод')
            vibor1 = input('Ваше дейтвие: ')
    except Exception:
        print('Неверный ввод')
    else:
        break
if vibor1 == '0':
    exit()
print('Выбери тип шифра: ')
print('1 - шифр Цезаря(по таблице ASCII)')
print('2 - азбука Морзе')
print('3 - шифровка двоичным кодом*')
print('*В шифровке двоичным кодом номер символа в таблице ASCII преобразуется в двоичный код(это число в двоичной системе и является шифром символа)')
vibor2 = input('Ваш выбор: ')
while True:
    if vibor2 == '1' or vibor2 == '2' or vibor2 == '3':
        break
    print('Неверный ввод')
    vibor2 = input('Ваш выбор: ')
vibor1 = int(vibor1)
vibor2 = int(vibor2)

if vibor2 == 1:
    while True:
        try:
            key = int(input('Введите ключ: '))
        except Exception:
            print('Неверный ввод')
        else:
            break
    polzov_otvet = input('Введите строку: ')
    list_otveta = list(polzov_otvet)
    otvet = ''
    if vibor1 == 1:
        for y in range(0,len(list_otveta)):
            orde = ord(list_otveta[y])
            orde += key
            list_otveta[y] = chr(orde)
        for r in list_otveta:
            otvet += r
        print('Результат: ',otvet)
    else:
        for i in range(0,len(list_otveta)):
            if list_otveta[i] == ' ':
                continue
            orde = ord(list_otveta[i])
            orde -= key
            list_otveta[i] = chr(orde)
        for t in list_otveta:
            otvet += t
        print('Результат: ',otvet)
if vibor2 == 2:
    print('В азбуке Морзе мы вместо точек будем использовать "*" вместо тире "-"')
    azbuka = ['*-','-***','*--','--*','-**','*','***-','--**','**','*---','-*-','*-**','--','-*','---','*--*','*-*','***','-','**-','**-*','****','-*-*','---*','----','--*-','--*--','-*--','-**-','**-**','**--','*-*-', ' ']
    alfavit = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','Ъ','ы','ь','э','ю','я',' ']
    if vibor1 == 1:
        print('Буквы будут написаны через пробел, слова через три пробела')
        polzov_otvet = input('Введите свое незашифрованное предложение(на русском): ')
        proveroch_list = list(polzov_otvet)        
        prov = 0
        while prov != 1: #этот цикл это проверка на правильность ввода
            prov = 1
            for b in proveroch_list:
                if alfavit.count(b) == 0:
                    polzov_otvet = input('Неверный ввод, попобуйте еще: ')
                    proveroch_list = list(polzov_otvet)
                    prov = 0
                    break               
        polzov_otvet = polzov_otvet.lower()
        list_otveta = polzov_otvet.split()
        shif_otvet = []
        for q in list_otveta:
            list_vremen = list(q)
            strok = ''
            for w in list_vremen:
                indx = alfavit.index(w)
                strok += str(azbuka[indx])
                strok += ' '
            shif_otvet.append(strok)
            shif_otvet.append('   ')
        print('Результат: ',*shif_otvet)
    if vibor1 == 2:
        polzov_otvet = str(input('Введите зашифрованную фразу: буквы в слове через пробел, слова запятую(пример: -**,** **,---*,*--*): '))
        proveroch_list = polzov_otvet.split(',')       
        prov = 0
        while prov != 1: #этот цикл это проверка на правильность ввода
            prov = 1
            for b in proveroch_list:
                proveroch_list2 = b.split(' ')
                for s in proveroch_list2:
                    if azbuka.count(s) == 0:
                        polzov_otvet = input('Неверный ввод, попобуйте еще: ')
                        proveroch_list = polzov_otvet.split(',')
                        proveroch_list2 = b.split(' ')
                        prov = 0
                        break
                if prov == 0:
                    break
        list_otveta = polzov_otvet.split(',')
        shif_otvet = []
        for z in list_otveta:
            list_vremen = z.split(' ')
            strok = ''
            for w in list_vremen:
                indx = azbuka.index(w)
                strok += str(alfavit[indx])
            shif_otvet.append(strok)
        print('Результат: ',*shif_otvet)
if vibor2 == 3:
    if vibor1 == 1:
        print('Буквы будут разделены через пробел, слова будут разделены тремя пробелами.')
        polzov_otvet = input('Введите свое незашифрованное предложение: ')
        list_otveta = polzov_otvet.split()
        shif_otvet = []
        for j in list_otveta:
            vrem_list = list(j)
            for v in range(0,len(vrem_list)):
                vrem_list[v] = ord(vrem_list[v])
            strok = ''
            for e in vrem_list:
                strok += bin1(e)
                strok += ' '
            strok += '   '
            shif_otvet.append(strok)
        print('Результат: ',*shif_otvet)
    if vibor1 == 2:
        polzov_otvet = input('Введите зашифрованную фразу: буквы в слове через пробел, слова запятую(пример: 100011101,10001 101001,11111): ')
        prover_vvod = ['0','1',',',' ']
        proveroch_list = list(polzov_otvet)
        print(proveroch_list)
        prov = 0
        while prov != 1: #этот цикл это проверка на правильность ввода
            prov = 1
            for b in proveroch_list:
                if prover_vvod.count(b) == 0:
                    polzov_otvet = input('Неверный формат ввода попобуйте еще: ')
                    proveroch_list = list(polzov_otvet)
                    prov = 0
                    break
        list_otveta = polzov_otvet.split(' ')
        shif_otvet = []
        strok = ''
        for x in list_otveta:
            list_vremen = x.split(',')
            strok = '' 
            for r in list_vremen:           
                list_num = list(r)
                per = bin_dec(list_num)
                strok += chr(per)      
            shif_otvet.append(strok)        
        print('Результат: ',*shif_otvet)

