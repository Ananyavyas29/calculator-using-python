def add(x,y):
        """This function adds two numbers"""
        return x+y
    
def substract(x,y):
        """This function substract two numbers"""
        return x-y
    
def multiply(x,y):
        """This function multiplies two numbers"""
        return x*y
    
def divide(x,y):
        """This function divide two numbers"""
        return x/y
    
def power(x,y):
        """This function gives power of two numbers"""
        return pow(x,y)
    
#taking input from user

print("select operation:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

choice=input("enter choice 1/2/3/4/5:")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
    
elif choice=='2':
    print(num1,"-",num2,"=",substract(num1,num2))
    
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
    
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
    
elif choice=='5':
    print(num1,"^",num2,"=",power(num1,num2))
    
else:
    print("invalid input")