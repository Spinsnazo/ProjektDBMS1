# Moduł wyświetlający łączne zużycie z liczników z podziałem na miejscowość odczytu

from matplotlib import pyplot as plt
from main.wynik import wynik as wynik


def raport():
    lista = wynik()
    # 3 - miejscowosc
    # 7 - wartosc odczytu
    #print(lista)
    dictt = dict()
    for rekord in lista:
        #print(rekord[3])
        dictt[rekord[3]] = dictt.setdefault(rekord[3], 0) + rekord[7]
    x, y = list(), list()
    for a, b in dictt.items():
        x.append(a)
        y.append(b)
    #print(dictt)
    plt.bar(x, y, align = 'center')
    plt.xlabel("Miejscowość")
    plt.xticks(rotation = 90)
    plt.ylabel("Łączne zużycie")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    raport()