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