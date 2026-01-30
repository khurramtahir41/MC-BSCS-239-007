
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

option = input("Enter option (1/2/3/4): ")

if option == "1":
    print("Result:", num1 + num2)

elif option == "2":
    print("Result:", num1 - num2)

elif option =="3":
    print("Result:", num1 * num2)

elif option =="4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")

else:
    print("Invalid option!")
