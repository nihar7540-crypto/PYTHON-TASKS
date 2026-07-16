for i in range (0,5):
    for j in range (i+1):
        print("*",end="")
    print("")

########################################################

for i in range (0,6):
    for j in range (1,i+1):
        print(j,end="")
    print("")    

########################################################

for i in range (5,-1,-1):
    for j in range (i+1):
        print("*",end="")
    print("")

########################################################

for i in range(1,6):
    for j in range(1,11):
        table=i*j
        print("{}*{}={}".format(i,j,table))
print("   ",end="  ")   

########################################################

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})")


######################## OPTIONAL ########################
num=int(input("enter a number: "))
for j in range(1,num+1):
    factor=0
    for i in range(1,j+1):
        if j%i==0:
            factor+=1
    if factor==2:
        print(j)

#################################################

n = int(input("Enter terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term

################################################
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print("GCD is:", a)    

