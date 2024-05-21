def get_user_input():
    input1 = input("chawere rame sityva: ")
    input2 = int(input("chawere rame ricxvi: "))
    return input1, input2

def analyze_inputs(input1, input2):
    type_input1 = type(input1)
    type_input2 = type(input2)
    return type_input1, type_input2

def print_results(type_input1, type_input2):
    print("sheni sityva aris", type_input1)
    print("sheni cipri aris", type_input2)

def calculate_and_print_result(operation, num1, num2):
    result = operation(num1, num2)
    print(result, type(result))

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

def concatenate_strings(string1, string2):
    return string1 + string2

def greet(name):
    print("Hello, " + name)

def calculate(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division

def main():
    # 4
    user_input1, user_input2 = get_user_input()
    analyzed_input1, analyzed_input2 = analyze_inputs(user_input1, user_input2)
    print_results(analyzed_input1, analyzed_input2)

    operations = [
        (1, '+', 1),
        (1, '-', 1),
        (1, '*', 1),
        (1, '/', 1)
    ]
    for operand1, operator, operand2 in operations:
        print(f"{operand1} {operator} {operand2} =", perform_operation(operand1, operator, operand2))

    # 5
    gela = "gela"
    gela2 = "chemi saxelia : "
    result = concatenate_strings(gela2, gela)
    print(result)

    # 6
    name = "Alice"
    greet(name)

    #7)
#Python-ის კონტექსტში, ტერმინი "ტერმინალი" ჩვეულებრივ ეხება Python-ის ინტერპრეტაციას, რომელიც მუშაობს ბრძანების ხაზის ინტერფეისის (CLI) გარემოში.
#ის მომხმარებლებს საშუალებას აძლევს პითონის კოდთან უშუალოდ ტექსტზე დაფუძნებული ბრძანებების საშუალებით ურთიერთქმედონ და მიიღონ დაუყოვნებელი გამოხმაურება.



    # 8
    cvladi1 = 2
    cvladi2 = 3
    result_add, result_sub, result_mul, result_div = calculate(cvladi1, cvladi2)
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

if __name__ == "__main__":
    main()