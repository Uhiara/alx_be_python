num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            # Exit the script or set a default result
            result = "undefined"
        else:
            result = num1 / num2
    case _:
        print("Invalid operation selected.")
        result = "undefined"
print(f"The result is: {result}")
