# 90+ : A
# 80–89 : B
# 70–79 : C
# 60–69 : D
# Below 60 : F

for i in range(5):
    grade=int (input("enter your grade out of 100:"))
    if grade >100:
        print("invalid input")
    elif grade<=100:
        if grade>=90:
            print("A grade")    
        elif grade>=80 and grade<=89:
            print("B grade")
        elif grade>=70 and grade<=79:
            print("C grade") 
        elif grade>=60 and grade<=69:
            print("D grade")  
        else:
            print("F grade")    

##############################################################
for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("c is greatest")
    elif a==c:
        print("a and c are equal")
        if b>a :
            print("c is greatest")
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c is greatest")
    elif a>b:
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
    else:
        print("all are equal")                  


##############################################################

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


#############################################################

for i in range(5):
    a=int(input("enter a number "))


    if a%2==0:
        print("number is even")
    else :
        print("number is odd")    


#############################################################

for i in range(5):
    num=int(input("enter number:"))
    if num>=0:
        if num>0:
            print("number is positive")
        elif num==0:
            print("number is zero")
    else:
        print("number is negative")            

    

#############################################################

a=int(input("enter 1st side of triangle: "))
b=int(input("enter 4th side of triangle: "))
c=int(input("enter 3rd side of triangle: "))
if a+b>c:
    print("this can be a triangle")
elif b+c>a:
    print("this can be a triangle")
elif a+c>b:
    print("this can be a triangle")    
else :
    print("this can't be a triangle")    

