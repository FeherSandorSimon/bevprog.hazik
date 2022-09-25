if __name__ == '__main__':
    number = input("Adjon meg egy számot: \n");

    unit_of_measure = input("")

    if number.isdigit():
        number = float(number);
    else:
        unit_of_measure = "invalid"

    inch = float(2.54)

    if "inch" in unit_of_measure:
        print(f"{(number * inch)} cm")
    elif "cm" in unit_of_measure:
        print(f"{(number / inch)} inches")
    else:
        print("Not correct unit!")

