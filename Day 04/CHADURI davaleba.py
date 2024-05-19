#დავალება:

#1. შექმენით ცვლადი რომელშიც შეინახავთ ნივთის ფასს. მეორე ცვლადში შეინახეთ ნივთის რაოდენობა.
#  თქვენი დავალებაა, რომ დაბეჭდოთ, თუ რამდენი უნდა გადაიხადოთ ნივთების ყიდვისას (ფასი * რაოდენობა)
#2. შექმენით ცვლადი, სადაც შეინახავთ თქვენს ასაკს. შემდეგ შექმენით მეორე ცვლადი,
#  სადაც შეინახავთ ნებისმიერი ოჯახისწევრის ასაკს. თქვენი დავალებაა, რომ ჯერ დაბეჭდოთ თქვენს ასაკს + 10, შემდეგ ოჯახისწევრის ასაკს + 10.
#3. შექმენით ორი ცვლადი, თითოეულში შეინახეთ ნებისმიერი რიცხვი. თქვენი დავალებაა,
#  რომ არითმეტიკული მოქმედებების შედეგი დაბეჭდოთ ამ რიცხვებს შორის - ეს მოქმედებებია +, -, *, /
#4. შექმენით ორი ცვლადი, პირველში თქვენი სახელი, ხოლო მეორეში ასაკი შეინახეთ. თქვენი
#  დავალებაა, რომ ჯერ სახელი დაბეჭდოთ, შემდეგ კი ასაკი.
#5. შექმენით ორი ცვლადი, პირველში შეინახეთ თქვენი ასაკი, ხოლო მეორეში შეინახეთ მშობლის ასაკი. 
# დაბეჭდეთ, თუ 10 წელში რამდენჯერ მეტი იქნება მშობლის ასაკი თქვენსაზე

cvladi=int(input("ნივთის ფასი: "))
meore_cvladi=int(input("ნივთის რაოდენობა: "))
print ("ნივთის ყიდვისას შენ უნდა გადაიხადო: ",  (cvladi) * (meore_cvladi), "ლარი")
#========================================================
asaki=int(input("რამდენი წლის ხარ?"))
ricxvi=10
print ("10 welshi shen iqnebi",  (asaki) + (ricxvi), "wlis")
meorecvlad=int(input("ramdeni wlisaa sheni ojaxiswevri? "))
ricxvi2=10
print ("shei ojaxis wevria: ",  (meorecvlad) + (ricxvi2), "wlis" )
print("nomeri sami davalebis pasuxia: ")
gela=2+2
gela2=3-2
gela3=3*2
gela4=6/3
print(gela+gela2-gela3*gela4/gela)
print("davaleba nomeri 4: ")
sheni_saxeli=input("chawere sheni saxeli: ")
sheni_asaki=int(input("chawere sheni asaki: "))
print("sheni saxelia: ", sheni_saxeli,",", " sheni asakia: ", sheni_asaki, "weli")
tqveni_asaki=int(input("chawere ramdeni wlis xar: "))
mshoblis_asaki2=int(input("chawere ramdeni wlis aris sheni mshobeli: "))

if mshoblis_asaki2>tqveni_asaki:
    print("10 welshi sheni mshobeli iqneba")
    print((mshoblis_asaki2 + 10) - (tqveni_asaki+10), "wlit didi tqvens asakze")
else:
    print("paps nu atyueeeb!!")
