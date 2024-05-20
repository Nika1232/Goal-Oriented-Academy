#8) მომხმარებელს შემოატანინეთ ორი რიცხვი და ყველა შესწავლილი ოპერატორით მოახდინეთ მათზე შედარებები.
def repeat1():
    choice="B"
    choice="b"
    if choice == "B" or choice == "b":
        momxmarebeli=int(input("chawere pirveli ricxvi "))
        momxmarebeli2=int(input("chawere meore ricxvi: "))
        print(momxmarebeli>momxmarebeli2)
        print(momxmarebeli>=(momxmarebeli2))
        print(momxmarebeli<=momxmarebeli2)
        print(momxmarebeli==(momxmarebeli2))
        print(momxmarebeli!=(momxmarebeli2))
        print(" ")
        def tryagain1(): 
            print("Type '1' to convert from the same number base")
            print("Type '2' to stop")
            r = input("Would you like to try again?")
            if r == '1':
                repeat1()
            elif r == '2':
                print("Thank you for using the BraCaLdOmbayNo Calculator!")
            else:
                print("You didn't enter any of the choices! Try again!")
                tryagain1()
        tryagain1()

repeat1()