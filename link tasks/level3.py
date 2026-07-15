add=0
num=int(input("enter a number for operation: "))
for i in range(1,num+1):
    add+=i
print("consecutive sum is",add)    
############################################################
for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a>b:
        if a>c:
            print("a is greatest")
        else:
            print("c is greatest")
    elif b>a:
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest")
    elif a>c:
        if a>b:
            print("a is greatest")
        else:
            print("b is greatest") 
    elif a==b:
            print("a and b are equal")  
        
else:
    print("all are equal")                  
############################################################
for i in range(5):
    year=int(input("enter year to check: "))
    if year%400==0:
        if year%4==0:
            print ("this is a leap year")
        elif year%100==0:
            print("not a leap year")    
        else:
            print("not a leap year")    
    else:
        print("not a leap year")        
############################################################
a=input("enter your username")
if a=="admin":
    b=int(input("enter your password"))
    if b==1234:
        print("login sucessfully")
    else :
        print("invalid password") 
else :
    print("invalid user name")           
###########################################################
a=int(input("enter a number: "))
if a%2==0:
    if a%4==0:
        print("its an even number and divisible by 4")
    elif a%4!=0:
        print("number is even but not divisible by 4")
else :
    print("not an even no")            
###########################################################
a=int(input("enter temperature in celcius"))
if a>=40:
    print("very hot")
elif a>=30 and a<40:
    print("hot")
elif a>=20 and a<30:
    print("normal")
else:
    print("cold")
###########################################################
