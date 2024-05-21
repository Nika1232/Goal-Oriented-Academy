# 4) შექმენით პითონის ფაილი და 4 ჯერ გამოიყენეთ print ფუნქცია, პირველ პრინტში გამოიყენეთ ორ რიცხვს შორის შეკრება +, მეორეში - გამოკლება, მესამეში * გამრავლება, მეოთხეში / გაყოფა
# 5) შეართეთ ორი ტექსტური მონაცემი და კომენტარებით ახსენით რა შედეგი მიიღეთ
# 6) დაუშვით ძალით შეცდომები და ნახეთ კომპიუტერი რას გამოგიტანთ შედეგად
# 7) ყველა დაწერილი კოდი ახსენით კომენტარები + (დოკუმენტში კომენტარების ამოყენებით ქართული ენით ახსენით რა არის ტერმინალი და რისთვის ვიყენებთ)
# 8) შექმენით 2 ცვლადი, შეინახეთ მასში რიცხვები და საბოლოოდ დაბეჭდეთ ამ ორ ცვლადს შორის რომელიმე არითმეტიკული მოქმედება
# 9) ახსენით კომენტარებით რა არის სტრინგი და რა არის მთელი რიცხვი

#4)
def perform_operation(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        return "Invalid operator"

# Define the operations
operations = [
    (1, '+', 1),
    (1, '-', 1),
    (1, '*', 1),
    (1, '/', 1)
]

# Iterate over the operations and print the results
for operand1, operator, operand2 in operations:
    print(f"{operand1} {operator} {operand2} =", perform_operation(operand1, operator, operand2))

#5)
def concatenate_strings(string1, string2):
    return string1 + string2

# Define the strings
gela = "gela"
gela2 = "chemi saxelia : "

# Concatenate the strings using the function
result = concatenate_strings(gela2, gela)

# Print the result
print(result)

#6)
def greet(name):
    print("Hello, " + name)

name = "Alice"
#grete(name)


#7)
#Python-ის კონტექსტში, ტერმინი "ტერმინალი" ჩვეულებრივ ეხება Python-ის ინტერპრეტაციას, რომელიც მუშაობს ბრძანების ხაზის ინტერფეისის (CLI) გარემოში.
#ის მომხმარებლებს საშუალებას აძლევს პითონის კოდთან უშუალოდ ტექსტზე დაფუძნებული ბრძანებების საშუალებით ურთიერთქმედონ და მიიღონ დაუყოვნებელი გამოხმაურება.


#8)
def calculate(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division

cvladi1 = 2
cvladi2 = 3

# Call the function
result_add, result_sub, result_mul, result_div = calculate(cvladi1, cvladi2)

# Print the results
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)


#9)
#1.
# "string" იგივე სტრიქონი: სტრიქონი არის სიმბოლოების თანმიმდევრობა, რომელიც ჩასმულია ერთ ბრჭყალებში (') ან ორმაგ ბრჭყალებში ("). სტრიქონები გამოიყენება პითონში ტექსტური მონაცემების წარმოსაჩენად.
# ისინი შეიძლება შეიცავდეს ასოებს, ციფრებს, სიმბოლოებს და თეთრ სივრცეს.
#2.
# მთელი რიცხვი: პითონში მთელ რიცხვებს მოიხსენიებენ, როგორც "integer". მთელი რიცხვი არის რიცხვი წილადი ნაწილის გარეშე.
# მთელი რიცხვები შეიძლება იყოს დადებითი, უარყოფითი ან ნულოვანი. ისინი წარმოდგენილია პითონში int მონაცემთა ტიპის გამოყენებით.