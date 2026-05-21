num1 = float(input("Insertt first number: "))
num2 = float(input("Enter second number: "))

operation = input("choose operation(+,-,*,/): ")
if operation == "+":
    result = num1 + num2
elif operation == "*":
    result = num1 * num2
elif operation == "-":
    result = num1 - num2
elif operation  == "/":
    result = num1 / num2
else:
    result = "Invalid choice"  
print("Result: ",result)        
     