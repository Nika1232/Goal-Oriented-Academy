#შემოატანინეთ მომხმარებელს ორი მნიშნელობა input() ფუნქციის მეშვეობით, შეინახეთ ისინი ცვლადებში ხოლო შემდეგ შეამოწმეთ
#  რა ტიპის მნიშვნელობები ინახება მოცემულ ცვლადებში type ფუნქციის გამოყენებით
#გააკეთეთ 10 მაგალითი 3 ტიპის გაყოფებზე  ესენია (/,//,%) იმუშავეთ და ნახეთ რა შედეგს დაგიბრუნებთ თითოეული გაყოფა

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

def main():
    # User input part
    user_input1, user_input2 = get_user_input()
    analyzed_input1, analyzed_input2 = analyze_inputs(user_input1, user_input2)
    print_results(analyzed_input1, analyzed_input2)

    # Calculation part
    calculate_and_print_result(lambda x, y: x / y, 10, 2)
    calculate_and_print_result(lambda x, y: x // y, 6, 2)
    calculate_and_print_result(lambda x, y: x % y, 5, 5)
    calculate_and_print_result(lambda x, y: x / y, 10, 10)
    calculate_and_print_result(lambda x, y: x // y, 6, 6)
    calculate_and_print_result(lambda x, y: x % y, 5, 6)

if __name__ == "__main__":
    main()