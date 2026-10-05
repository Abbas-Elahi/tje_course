print("🛸 SPACE CALCULATOR 🛸")
number1 = float(input("First number: "))
operator = input("+  -  *  / : ")
number2 = float(input("Second number: "))
if operator == "+":
    answer = number1 + number2
elif operator == "-":
    answer = number1 - number2
elif operator == "*":
    answer = number1 * number2
elif operator == "/":
    answer = "Cannot divide by zero" if number2 == 0 else number1 / number2
else:
    answer = "Unknown command 🤖"
print("Answer =", answer)
