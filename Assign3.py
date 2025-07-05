#Factorial
num = int(input("Enter a number"))
fact = 0
def factorial(num):
    if num == 0:
        return 1

    else:
        fact = num*(num-1)
        print("Factorial of {} is: {}".format(num,fact))

factorial(num)



#Math operations
num=int(input("Enter a number"))
import math
print("Square root: ",math.sqrt(num))
print("Logarithm :",math.log(num))
print("Sine: ",math.sin(num))
