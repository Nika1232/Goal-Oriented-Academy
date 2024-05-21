def DAVALEBIS_DAWERA():
    momxmarebeli = int(input("chawere pirveli ricxvi: "))
    momxmarebeli2 = int(input("chawere meore ricxvi: "))
    print(momxmarebeli > momxmarebeli2, momxmarebeli >= momxmarebeli2, momxmarebeli <= momxmarebeli2, momxmarebeli == momxmarebeli2, momxmarebeli != momxmarebeli2, "\nType '1' to convert from the same number base\nType '2' to stop")
    r = input("Would you like to try again? ")
    if r == '1':
        DAVALEBIS_DAWERA()
    elif r != '2':
        print("You didn't enter any of the choices! Try again!")
        DAVALEBIS_DAWERA()

DAVALEBIS_DAWERA()