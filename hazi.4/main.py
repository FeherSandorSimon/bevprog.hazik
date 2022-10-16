class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.feladatkor = szerepkor

        print("-- Developer létrehozva --")
        print(self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben.")

    def __str__(self):
       return self.nev+" a "+self.projekt+"-en dolgozik "+self.feladatkor+" szerepkörben."

    def __eq__(self, other):
        return self.nev == other.nev and self.projekt == other.projekt and self.feladatkor == other.feladatkor

def check():
    developers = [Team("Ricsi","SolArch","Frontend"),Team("Angéla","ZerTeng","Tesztelő"),Team("Peti","KefERP","Backend"),Team("Éva","KefERP","Frontend")]

    print()
    gyujtd = []
    for x in range(0,len(developers)):
        for y in range(0, len(developers)):
            if y == x:
                pass

            elif developers[x].projekt == developers[y].projekt and y > x:

                print(developers[x].nev+" és "+developers[y].nev+" dolgoznak egy projekten.")



    szurve = []
    [szurve.append(x) for x in gyujtd if x not in szurve]


    megvoltak = []
    for x in range(0,len(szurve)):
        for y in range(0,len(szurve)):
            if x != y and (szurve[y] not in megvoltak) and szurve[x].projekt == szurve[y].projekt:
                megvoltak.append(szurve[x])
                print(szurve[x].nev + " és " + szurve[y].nev + " dolgoznak egy projekten")

if __name__ == "__main__":
    check()