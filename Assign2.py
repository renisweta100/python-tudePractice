
#Odd OR Even
num = int(input("Enter a number"))
if num%2==0:
    print("{} is an even number.".format(num))

else:
    print("{} is an odd number.".format(num))



#sum 1 to 50
sum = 0

for i in range(51):
    sum = sum+i

print("The sum of numbers from 1 to 50 is: ",sum)