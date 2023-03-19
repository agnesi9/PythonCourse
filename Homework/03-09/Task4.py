number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))
operator = input("Enter one of the following operators: *,/,+,-,%: ")

while (operator == "*" or operator == "/" or operator == "+" or operator == "-" or operator == "%")==False:
    print("Operation provided isn't valid, please,try again")
    operator = input("Enter one of the following operators: *,/,+,-,%: ")

if operator == "*":
    calc = number1*number2
elif operator == "/":
    calc = number1/number2
elif operator == "+":
    calc = number1+number2
elif operator == "-":
    calc = number1-number2
elif operator == "%":
    calc = number1%number2

print(calc)


