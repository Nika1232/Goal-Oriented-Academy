import time

#შემოატანინეთ მომხმარებელს ორი მნიშნელობა input() ფუნქციის მეშვეობით, შეინახეთ ისინი ცვლადებში ხოლო შემდეგ შეამოწმეთ
#  რა ტიპის მნიშვნელობები ინახება მოცემულ ცვლადებში type ფუნქციის გამოყენებით
input1=input("chawere rame sityva: ")
input2=int(input("chawere rame ricxvi: "))
print ("sheni sityva aris", type(input1))
print ("sheni cipri aris", type(input2))
time.sleep(2)
#გააკეთეთ 10 მაგალითი 3 ტიპის გაყოფებზე  ესენია (/,//,%) იმუშავეთ და ნახეთ რა შედეგს დაგიბრუნებთ თითოეული გაყოფა
def gela():
    gela1 = 10/2
    print(gela1,type(gela1))
    gela2=6//2
    print(gela2,type(gela2))
    gela3=5%5
    print(gela3,type(gela3))
    gela4 = 10/10
    print(gela4,type(gela4))
    gela5=6//6
    print(gela5,type(gela5))
    gela6=5%6
    print(gela6,type(gela6))


gela()