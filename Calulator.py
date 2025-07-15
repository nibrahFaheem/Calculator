print("which operation do you want to perform?" \
"a.addition,\nb.subtraction,\nc.multiplication, \nd.division," \
"\ne.exponentiation\n"
"Please enter your choice: ", end='')
operation = input().strip().lower()
if operation == "a":
    print("You chose addition.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The result is: {result}")   
elif operation == "b":
    print("You chose subtraction.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "c":
    print("You chose multiplication.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "d":
    print("You chose division.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result is: {result}")   
elif operation == "e":
    print("You chose exponentiation.")
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print(f"The result is: {result}")       
else:
    print("Invalid operation. Please choose from addition, subtraction, multiplication, division, or exponentiation.")
print("Thank you for using the calculator!")    
