from index import menu,RNG

while True:
    m1=menu.menu_1()

    if m1 == 0:
        break
    elif m1 in range(1,20):
        while True:
            m2=menu.menu_2()
            if m2 == 0:
                break
            elif m2 in range(1,6):
                RNG.test(m1,m2)
            else:
                print('Numero invalido "Y"')
    else:
        print('Numero invalido "X"')

