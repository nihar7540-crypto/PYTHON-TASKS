arr=[]
for i in range(3):
    lst=[]
    for j in range(3):
        b=int(input(f"enter the element for column {j+1} and row {i+1}: "))
        lst.append(b)
    arr.append(lst)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()

##################################################################################

arr=[]
for i in range(2):
    lst=[]
    for j in range(3):
        b=int(input(f"enter the element for row {j+1} and column {i+1}: "))
        lst.append(b)
    arr.append(lst)
transarrr=[]
for j in range(3):
        transarr=[]
        for i in arr:
            transarr.append(i[j])
        transarrr.append(transarr)
print("original 2x3 matrix")
for i in arr:
    for j in i:
        print(j,end=" ")
    print()
print()
print("transposed 3x2 matrix")
for i in transarrr:
    for j in i:
        print(j,end=" ")
    print()

##################################################################################

arr=[]
combined1d=[]
for i in range(3):
    lst=[]
    for j in range(3):
        a=int(input(f"enter element for row {i+1} and col {j+1}: " ))
        lst.append(a)
    arr.append(lst)
for i in arr:
    sum=0
    for j in i:
        sum+=j
    print(sum)
    combined1d.extend(i)
print("max :",max(combined1d))
print("min :",min(combined1d))
combined1d.sort()
print(combined1d)
combined1d.reverse()
print(combined1d)

##################################################################################

a=[(12,324,4343,3),(31,45,21,5,23451,37),(213,23,3,13,1,41)]
sorteda=[]
for i in a:
        sorteda.append((i[1],i))
b=sorted(sorteda)
finals=[]
for i in sorteda:
    finals.append(i[1])
print(finals)

##################################################################################

students = [{"name": "Rahul", "age": 22},{"name": "Anjali", "age": 19},{"name": "Vikram", "age": 21}]
temp=[]
for i in students:
    temp.append((i["age"],i))
b=sorted(temp)
finalsorted=[]
for i in b:
    finalsorted.append(i[1])
print(finalsorted)

##################################################################################

lst=[213,1242,34,234,32452,36,46,5,677]
lst.sort()
a=sorted(lst)
print(lst)
print(a)

