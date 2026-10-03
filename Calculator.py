def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("Sum:", add(num1, num2))
print("Difference:", sub(num1, num2))
print("Product:", mul(num1, num2))
print("Quotient:", div(num1, num2))