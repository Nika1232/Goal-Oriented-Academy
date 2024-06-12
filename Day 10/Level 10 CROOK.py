# გაიარეთ for ციკლი და გააკეთეთ 5 მაგალითი for ციკლებზე
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#  for ციკლის მეშვეობით შეასრულეთ ყველა მათემატიკური ოპერაცია 0-დან 100-მდე რიცხვებზე

num = 4
for i in range(100):
    print(i + num)

for i in range(100):
    print(i - num)

for i in range(100):
    print(i / num)

for i in range(100):
    print(i * num)

for i in range(100):
    print(i < num)

for i in range(100):
    print(i > num)

#  მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვამდე ყველა
#  რიცხვის ჯამი(მაგალითად თუ შეიყვანს 10ს გამოიტანეთ 10მდე ყველა რიცხვის ჯამი მაგალითად).

num = int(input("შეიყვანეთ რიცხვი: "))

total_sum = 0

for i in range(num + 1):
    total_sum += i

print("0-dan " + str(num) + "-mde ricxvebis jami aris: " + str(total_sum))

#  მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი.

ricxvi1 = int(input("chawere pirveli ricxvi: "))
ricxvi2 = int(input("chawere meore ricxvi: "))

result_multiply = ricxvi1 * ricxvi2
result_add = ricxvi1 + ricxvi2

for i in range(1):  
    print("namravli:", result_multiply)
    print("jami:", result_add)