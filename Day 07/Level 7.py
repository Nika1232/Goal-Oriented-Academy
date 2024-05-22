#შექმენით ალგორითმი, რომელიც მომხმარებელს შეეკითხება ტემპერატურას ცელსიუსში და გადაიყვანს ფარენჰეიტში. ((variable * 1.8) + 32)
algoritmi=int(input("chawere ramdenia temperatura: "))
#Formula:	(°C × 9/5) + 32 = °F
Fahrenheit=algoritmi * 9/5 + 32
print("printing result... ",Fahrenheit)

#მომხმარებელს შეეკითხეთ ასაკი და მოახდინეთ შედარება ისე, რომ ასაკი ნაკლები იყოს ოცზე და მეტი იყოს თორმეტზე.
def SH():
    shekitxva=int(input("ramdeni wlis xar?: "))
    gela=("gela")
    if shekitxva<20 and shekitxva>12:
        return shekitxva<20,shekitxva>12, "martalia, martalia, rom sheni asaki 20 welze naklebia da 12 welze metia "
    else:
        return "sheni asaki ar aris 12dan 20 wlamde"
result = SH()
print(result)

# მომხმარებელს შემოატანინეთ მართკუთხედის (rectangle) გვერდები (გაითვალისწინეთ, რომ შესაძლოა რიცხვი ათწილადიც იყოს) და დაუბეჭდეთ მისი ფართობი.
# Area's formula=Length×Width
# mezareba defis ageba hintebis gareshe so ill just do this :d
sigrdze=float(input("chawere martkutxedis sigrdze: "))
sigane=float(input("chawere martkutxedis sigane: "))
Area=sigrdze*sigane
print("shens mier sheqmnili martkutxedis partobia: ",Area)

#მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ არის თუ არაrის 100-ზე მეტი და 9-ის ჯერადი (9-ზე სრულად იყოფა). გამოიყენეთ And ოპერატორი
user = int(input("chawere ricxvi: "))
def SH2():
    message = ""
    if user%9!=0:
        message += "ricxvis nashti ar aris 0. magram 100ze naklebia. "
    if user<0:
        message += "ricxvi naklebia 100ze. "
    if user == 0:
        return "ricxvi udris 0"
    if user<100 and user%9==0:
        message += "ricxvi iyopa 9ze da nashtic aris 0 aseve ricxvi aris 100ze naklebi. "
    if user<100 and user>0:
        message += "ricxvi naklebia 100 ze da metia 0 ze. "
    else:
        message = "ricxvi ar aris 100ze naklebi. "
    return message

result2 = SH2()
print(result2)

# 2 SAATI MOVUNDI AM KODIS GASWOREBAS :@:@ wesit modulebis daxmarebit amdens ar viwvaleb da uketessac gavaketeb :D 
