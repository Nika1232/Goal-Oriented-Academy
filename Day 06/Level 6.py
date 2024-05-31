def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    # Input four numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    num4 = float(input("Enter fourth number: "))

    # Perform arithmetic operations
    result1 = add(num1, num2)
    result2 = subtract(num3, num4)
    result3 = multiply(num1, num3)
    result4 = divide(num2, num4)

    # Print the results
    print(f"{num1} + {num2} = {result1}")
    print(f"{num3} - {num4} = {result2}")
    print(f"{num1} * {num3} = {result3}")
    print(f"{num2} / {num4} = {result4}")

    # Compare the results of the first two operations
    if isinstance(result1, (int, float)) and isinstance(result2, (int, float)):
        if result1 > result2:
            print(f"{result1} is greater than {result2}")
        elif result1 < result2:
            print(f"{result2} is greater than {result1}")
        else:
            print(f"{result1} is equal to {result2}")

def registration_simulation():
    print("Welcome to the Registration Simulation!")
    print("Please provide the following information:")

    # Input user details
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input. Please enter a valid age.")

    email = input("Enter your email address: ")

    # Print the entered information
    print("\nRegistration Details:")
    print(f"Name: {name}")
    print(f"Last Name: {last_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

def congratulate_user():
    # Ask for the user's name
    name = input("Enter your name: ")
    
    # Print a congratulatory message
    print(f"gilocav {name}! ")

def calculate_future_ages():
    # Ask for the parent's ages
    father_age = int(input("Enter your father's age: "))
    mother_age = int(input("Enter your mother's age: "))
    
    # Calculate the ages after 20 years
    father_age_future = father_age + 20
    mother_age_future = mother_age + 20
    
    # Print the results
    print(f"In 20 years, your father will be {father_age_future} years old.")
    print(f"In 20 years, your mother will be {mother_age_future} years old.")

def user_information():
    # სთხოვეთ მომხმარებელს შეიყვანოს ინფორმაცია თავის თავზე
    name = input("შეიყვანეთ თქვენი სახელი: ")
    surname = input("შეიყვანეთ თქვენი გვარი: ")
    age = input("შეიყვანეთ თქვენი ასაკი: ")
    address = input("შეიყვანეთ თქვენი მისამართი: ")
    gmail = input("შეიყვანეთ თქვენი ელ.ფოსტა: ")
    
    # დაბეჭდეთ ინფორმაცია ერთ დიდ წინადადებად
    print(f"თქვენი სახელი არის {name}, გვარი - {surname}, ასაკი - {age} წელი, მისამართი - {address}, და თქვენი ელ.ფოსტა არის {gmail}.")

def main():
    print("Select an option:")
    print("1. Calculator")
    print("2. Registration Simulation")
    print("3. Congratulate User")
    print("4. Calculate Future Ages of Parents")
    print("5. User Information")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        registration_simulation()
    elif choice == "3":
        congratulate_user()
    elif choice == "4":
        calculate_future_ages()
    elif choice == "5":
        user_information()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
