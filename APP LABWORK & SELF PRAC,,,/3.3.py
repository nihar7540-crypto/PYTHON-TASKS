# from _typeshed import importlib
# from _typeshed import importlib
# from _typeshed import importlib
# while True:
#     num=int(input("enter number: "))
#     if num==0:
#         break

# #################################################
# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1

# ##################################################

# for i in range(1,20+1):
#     if i%2!=0:
#         print(i)

# ##################################################

# for i in range(5,50+1,5):
#     print(i)

# #################################################

# for i in range(10,0,-1):
#     print(i)

# #################################################

# for i in range(1,10+1):
#     sq=i**2
#     print(sq)

# #################################################

for i in range (1,50+1):
    if i%3==0 and i%2!=0:
        print(i,"divisible by 3 only")
    elif i%2==0 and i%3!=0:
        print(i,"divisible by 2 only")
    else:
        print(i,"divisible by neither 2 nor 3")
        