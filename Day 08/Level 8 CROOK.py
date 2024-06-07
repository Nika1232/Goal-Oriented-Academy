# 3) შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 5 რციხვს, ხოლო ამ 5 რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია (+,-,*,/,%,//),
#  საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში + ახსენით თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს.
# 4) შემოატანინეთ მომხარებელს ასაკი და შეამოწმეთ არის თუ არა 18 წელზე მეტის და 20 წელზე ნაკლების მიღებული შედეგი დაპრინტეთ
# 5)  ჩამოწერეთ ხუთ-ხუთი მაგალითი ყველა ლოგიკურ ოპერატორზე > ,<, <=, >=, !=, == 
# 6) ომხმარებელს პირველ ინფუთში მთელი რიცხვი, ხოლო მეორე ინფუთში ათწილადი შემოატანინეთ. საბოლოოდ შეადარეთ ცვლადების მნიშვნელობების მონაცემთა ტიპები 
# 7)  შექმენით რამოდენიმე სხვადასხვა ტიპის ცვლადი და დაბეჭდეთ მათი მონაცემთა ტიპები


# qwer1=int(input("chawere pirveli ricxvi: " )) #sheaqvs pirveli ricxvi da imitom davwere ro davalebad mqonda
# qwer2=int(input("chawere meore ricxvi: " )) #sheaqvs meore ricxvi da imitom davwere ro davalebad mqonda
# qwer3=int(input("chawere mesame ricxvi: " )) #sheaqvs mesame ricxvi da imitom davwere ro davalebad mqonda
# qwer4=int(input("chawere meotxe ricxvi: " )) #sheaqvs meotxe ricxvi da imitom davwere ro davalebad mqonda
# qwer5=int(input("chawere mexute ricxvi: " )) #sheaqvs mexute ricxvi da imitom davwere ro davalebad mqonda
# qwer6=qwer1*qwer2/qwer3//qwer4-qwer5+qwer1%qwer5 # am 5 ricxvs shoris asrulebs yvela aritmetikul operaciebs da imitom davwere ro davalebad mqonda
# print(qwer6) #ekranze gamoaqvs qwer6 shi rac weria(6 lineze) da imitom davwere ro davalebad mqonda

asaki=int(input("chawere ramdeni wlis xar: ")) #vekitxebi momxmarebels tu ramdeni wlis aris da imitom davwere ro davalebad mqonda
asaki2=asaki<20, asaki>18 #vamowmeb tu aris 18 welze metis da 20 welze naklebis da imitom davwere ro davalebad mqonda
print(asaki2) #vprintav migebul shedegs da imitom davwere ro davalebad mqonda

#def chamovwere da davprinte xut xuti magaliti yvela logikur operatorze(> ,<, <=, >=, !=, ==) da imitom davwere ro davalebad mqonda():
result1_1 = 5 > 3
result1_2 = 10 > 7
result1_3 = 2 > 5
result1_4 = -1 > -5
result1_5 = 100 > 50

result2_1 = 3 < 5
result2_2 = 7 < 10
result2_3 = 5 < 2
result2_4 = -5 < -1
result2_5 = 50 < 100

result3_1 = 3 <= 5
result3_2 = 7 <= 10
result3_3 = 5 <= 5
result3_4 = -5 <= -1
result3_5 = 50 <= 100

result4_1 = 5 >= 3
result4_2 = 10 >= 7
result4_3 = 5 >= 5
result4_4 = -1 >= -5
result4_5 = 100 >= 50

result5_1 = 5 != 3
result5_2 = 10 != 7
result5_3 = 5 != 5
result5_4 = -1 != -5
result5_5 = 100 != 50

result6_1 = 5 == 5
result6_2 = 10 == 10
result6_3 = 5 == 3
result6_4 = -1 == -1
result6_5 = 100 == 50

print(result1_1, result1_2, result1_3, result1_4, result1_5)
print(result2_1, result2_2, result2_3, result2_4, result2_5)
print(result3_1, result3_2, result3_3, result3_4, result3_5)
print(result4_1, result4_2, result4_3, result4_4, result4_5)
print(result5_1, result5_2, result5_3, result5_4, result5_5)
print(result6_1, result6_2, result6_3, result6_4, result6_5)

# 6) ომხმარებელს პირველ ინფუთში მთელი რიცხვი, ხოლო მეორე ინფუთში ათწილადი შემოატანინეთ. საბოლოოდ შეადარეთ ცვლადების მნიშვნელობების მონაცემთა ტიპები 
input1=int(input("chawere mteli ricxvi: "))
input2=float(input("chawere atwiladi: "))
print(input1>input2,input1<input2)

# 7)  შექმენით რამოდენიმე სხვადასხვა ტიპის ცვლადი და დაბეჭდეთ მათი მონაცემთა ტიპები
print(type(1))
print(type(2.5))
print(type("gela"))