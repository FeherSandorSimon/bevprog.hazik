if __name__ == '__main__':

        while True:
                try:
                        a = int(input("Enter 'a' value: "))
                        b = int(input("Enter 'b' value: "))
                        print(a / b)
                        print("Out of try except blocks")
                except:
                        if b == 0:
                                print("Division by zero not allowed")
                                print("Out of try except blocks")

                        break