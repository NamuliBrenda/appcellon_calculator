

def add(x, y):
	return x + y
	

def subtract(x, y):
	return x - y
	

def multiply(x, y):
	return  x * y
	

def divide(x, y):
	return x / y
	

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice between (1/2/3/4)")

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
                        

if choice == '1':
	print("result is", add(num1,num2))
elif choice == '2':
	print("result is", subtract(num1,num2))
elif choice == '3':
	print("result is", multiply(num1,num2))
elif choice == '4':
	print("result is", divide(num1,num2))
else:
	print("Invalid input")
	










