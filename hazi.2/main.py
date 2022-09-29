if __name__ == '__main__':
    print(" Adja meg a háromszög három oldalát cm-ben: ")
    a = int(input(" a oldal (cm): "))
    b = int(input(" b oldal (cm): "))
    c = int(input(" c oldal (cm): "))

    if a + b > c and a + c > b and b + c > a:
        print(" A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög szerkeszthető. ")
    else:
        print(" A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög NEM szerkeszthető. ")
