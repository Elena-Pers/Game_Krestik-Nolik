
field = [['-']*3 for _ in range(3)]

#------Отрисовка игрового поля
def show(f):
    print('  0 1 2')
    for i in range(len(field)):
         print (str(i)+' '+ ' '.join(field[i]))

#------Функция заполнения Х или О
def users(f):
    while True:
        place = input('Введите две координаты через пробел:  ').split()
        if len(place) !=2:
            print('Неверно. Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Неверно. Введите числа')
            continue
        x,y=map(int, place)
        if not (x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята. Введите координаты')
            continue
        break
    return x,y

#----------- Функция определения победителя
def win(f, user):
    def check_line (a1, a2, a3, user):
         if a1==user and a2==user and a3==user:

            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
        check_line(f[0][n], f[1][n], f[2][n], user) or \
        check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

count=0
#----------- Раскраска Х и О в красный и синий цвета
while True:
    show(field)
    if count%2 == 0:
        user="\033[31m{}\033[0m".format('x')
    else:
        user="\033[34m{}\033[0m".format('o')


    x,y=users(field)
    field[x][y]=user

    count += 1
    if win(field, user):
        show(field)
        print(f"Поздравляем! Выиграл {user}")
        break

    if count==9:
        print('Ничья! Игра окончена')
        show(field)
        break

    print("Количество ходов: ", count)




