items=[]
s=int(input("enter array size: "))
print("enter array elements:")
for i in range(s):
    i=int(input(f"a[{i}]="))
    items.append(i)
lenn=0
for i in items:
    lenn+=1
print(lenn)

################################################################

items=[]
s=int(input("enter array size: "))
print("enter array elements:")
for i in range(s):
    v=int(input(f"a[{i}]="))  
    items.append(v)           
summ=0
for i in items:
    summ+=i
lenn=0
for i in items:
    lenn+=1
print("average is ", summ/lenn) 

#################################################################

items=[]
items2=[]
finalarr=[]
s=int(input("enter array size: "))
print("enter array 1 elements:")
for i in range(s):
    v=int(input(f"a[{i}]="))  
    items.append(v) 
print("enter array 2 elements:")
for j in range(s):
    z=int(input(f"a[{j}]="))  
    items2.append(z) 
for i in range(s):
    add = items[i] + items2[i]
    finalarr.append(add) 
print(finalarr)

#################################################################

arr=[1,2,3,4,5,6,7,8,9,10]
for i  in arr:
    print(f"{i} * 2 = ",i*2)

#################################################################

arr=[]
for i in range(5):
    a=int(input("enter the elements: "))
    arr.append(a)
print(arr)
b=int(input("enter the element to find :"))
if b in arr:
    print("element found and its index is ",arr.index(b))
else:
    print("element not found")

#################################################################

arr=[]
earr=[]
oarr=[]
for i in range(5):
    a=int(input("enter the elements: "))
    arr.append(a)
print(arr)
for j in arr:
    if j%2==0:
        earr.append(j)
    elif j%2!=0:
        oarr.append(j)
print(earr)
print(oarr)

#################################################################

arr=[]
for i in range(10):
    a=int(input("enter the elements: "))
    arr.append(a)
print(arr)
print(arr[:5])
print(arr[::2])
print(arr[0])
print(arr[-1])
print(arr[(len(arr)//2)])

      


    
