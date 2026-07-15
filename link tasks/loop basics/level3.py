fact=1
n=int(input("enter a number: "))
for i in range(n,1,-1):
    fact*=i
print(fact)    

#####################################################3

sum=0
n=int(input("enter a number: "))
for i in range(1,n+1):
    sum+=i
print(sum)    

######################################################

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10
print("Reversed number:", reversed_num)

###################################################3#3

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10
if num==reversed_num:
    print("its a palindrome")
else:
    print("not a palindrome")

######################################################

sum=0
num = int(input("Enter a number: "))
while num>0:
    remain=num%10
    sum+=remain
    num=num//10
print(sum)
    
