def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for operation
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        print("Invalid operation. Please try again.")
    
    # Get user input for numbers
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    # Perform calculation based on operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
    
    # Print result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()