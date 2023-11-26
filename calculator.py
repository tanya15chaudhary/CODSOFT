#calculator
#function to add two numbers
def add(num1,num2):
    return num1+num2

#fu nction to subtract two numbers
def subtract(num1,num2):
    return num1-num2

#function to multiply two numbers
def multiply(num1,num2):
    return num1*num2

#function to divide two numbers
def divide(num1,num2):
    return num1/num2

print("Select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

#take input from the user
select = int(input("select operation from 1,2,3,4"))
num1= int(input("enter first number"))
num2= int(input("enter second number"))

if select ==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif select==2:
    print(num1,"-",num2,"=",subtract,(num1,num2))

elif select==3:
    print(num1,"*",num2,"=",multiply,(num1,num2))
    
elif select==2:
    print(num1,"-",num2,"/",divide,(num1,num2))

else:
    print("Invalid input")

