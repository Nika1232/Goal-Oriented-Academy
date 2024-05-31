1)
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

# Call the calculator function
calculator()

2)def registration_simulation():
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

if __name__ == "__main__":
    registration_simulation()


