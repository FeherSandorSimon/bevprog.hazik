with open("Rózsi néni.txt", "r") as f:
    for sor in f:

        szoveg = sor.strip().replace("-", "").replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace(" ","").replace("a", "").replace("á", "").replace("e", "").replace("é", "").replace("i", "").replace("í", "").replace("o", "").replace("ó", "").replace("ö", "").replace("ő", "").replace("u", "").replace("ú", "").replace("ü", "").replace("ű","").replace("A", "").replace("Á", "").replace("E", "").replace("É", "").replace("I", "").replace("Í", "").replace("O","").replace("Ó", "").replace("Ö", "").replace("Ő", "").replace("U", "").replace("Ú", "").replace("Ü", "").replace("Ű", "")

        if szoveg != "":

            print(szoveg)
