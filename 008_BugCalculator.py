print("Bug Calculator")

num1 = float(input("Enter first number: "))
op = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Cannot divide by zero buggy!"
    else:
        result = num1 / num2
else:
    result = "Invalid operator bro."

print(f"Result: {result}")