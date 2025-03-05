import math
print (" CALCULATOR ")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error! Division by zero is not allowed."
    else:
        return a/b
def pow(a,b):
    return a**b
def sqrt(a):
    if a<0:
        return "Error! Square root of negative number is not allowed."
    else:
        return math.sqrt(a)
def logi(a,b):
    if a<=0 or b<=0:
        return "Error! Logarithm of non-positive number is not allowed."
    else:
        return math.log(a)/math.log(b)
    
while True:
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Exponentiation")
    print ("6. Square root")
    print ("7. Logarithm")
    print ("8. Exit")
    choice = int(input("Enter your choice (1-8): "))
    if choice in [1,2,3,4,5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice==1:
            print (f"{num1}+{num2}={add(num1,num2)}")
        if choice==2:
            print (f"{num1}-{num2}={sub(num1,num2)}")
        if choice==3:
            print (f"{num1}*{num2}={mul(num1,num2)}")
        if choice==4:
            print (f"{num1}/{num2}={div(num1,num2)}")
        if choice==5:
            print (f"{num1}^{num2}={pow(num1,num2)}")

    elif choice == 6:
        num1 = float(input("Enter number: "))
        print (f"Square root of {num1}={sqrt(num1)}")

    elif choice == 7:
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter base: "))
        print (f"Logarithm of {num1} with base {num2}={logi(num1,num2)}")
    elif choice ==8:
        print (" Exiting the calculator ")
        break
    else:
        print ("Invalid choice")
