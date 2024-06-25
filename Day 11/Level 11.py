print("airchie romeli moqmedeba gsurs: ")
print("1. mimateba (+)")
print("2. gamokleba (-)")
print("3. gamravleba (*)")
print("4. gayopa (/)")

choice = input("chawere ricxvi 1 , 2 , 3 an 4 rata airchio moqmedeba : ")

num1 = float(input("chawere pirveli cipri: "))
num2 = float(input("chawere meore cipri: "))

# tu chawer ertians rezulti iqneba pirveli cipris mimateba meore ciprtan
if choice == '1':
    result = num1 + num2
    operation = '+'
# an tu chawer orians mashin rezulti iqneba 2 ciprs shoris sxvaoba
elif choice == '2':
    result = num1 - num2
    operation = '-'
# gamravleba
elif choice == '3':
    result = num1 * num2
    operation = '*'
# gayopa
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = '/'
    # tu nomeri udris 0 mashin daprintavs erors
    else:
        result = "error"
# sxva nebismier shemtxvevashi daprintavs erors da gatishavs scripts
else:
    print("error")
    exit()


print(str(num1) + " " + operation + " " + str(num2) + " = " + str(result))
