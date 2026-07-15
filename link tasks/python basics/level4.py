for i in range(1,10+1):
    print(i)
#######################################################################
for i in range(10+1,1,-1):
    print(i)
#######################################################################
n=int(input("enter number for multiplication ;"))
for i in range(1,10+1):
    tab=n*i 
    print("{}*{}={}".format(n,i,tab))    
#######################################################################
n=int(input("enter number :"))
sum=0
for i in range (0,n+1):
    sum+=i
print(sum)    
#######################################################################
number=int(input("enter a number of multiple digits"))
digit_count = 0
while number > 0:
    number = number // 10  
    digit_count += 1       
print("Total digits:", digit_count)
#######################################################################
#######################################################################