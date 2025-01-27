




def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def divide(a, b):
  if b != 0:
    return a / b
  else:
    print("Error cannot divide by 0!")



print("please select one of the following options:")
print("1. add")
print("2. subtract")
print("3. multiplication")
print("4. division")


UserOperation = input("your selection: ")

num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))



if UserOperation == '1':
  print(f"Answer: {add(num1, num2)}")
  
elif UserOperation == '2':
  print(f"Answer: {subtract(num1, num2)}")

elif UserOperation == '3':
  print(f"Answer: {multiplication(num1, num2)}")

elif UserOperation == '4':
  print(f"Answer: {divide(num1, num2)}")
  
else:
  print("invalid input")

