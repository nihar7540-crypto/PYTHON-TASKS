a=["apple", "banana", "cherry"]
count=0
for i in a :
    for j in i:
        if j in "aeiouAEIOU":
            count+=1
print(count)

##################################################

b=["hello", "world"]
revb=[]
for i in b:
    revb.append(i[::-1])
print(revb)

##################################################

b=["cat", "elephant", "dog"]
c=max(b)
print(c)

##################################################

a = ["hello", "banana"]
result = []  
for i in a:
    char = list(i)
    for j in char:
        if char.count(j) > 1:
            char.remove(j)
    word = "".join(char)
    result.append(word)
print(result)

###################################################

a=["apple", "dog", "elephant"]
for i in a:
    if i[0] not in "aeiouAEIOU":
        a.remove(i)
print(a)

###################################################

a=["Python", "is", "fun"]
print(" ".join(a))

##################################################

a = ["bella", "label", "roller"]
result = []  
for j in a[0]:
    if j in a[1] and j in a[2]:
        result.append(j)      
print(set(result))

##################################################

a= ["Python is fun", "I love coding"]   
b=a[0].split()
c=a[1].split()
print(b+c)

##################################################

a=["madam", "hello", "racecar"]
b=[]
for i in a :
    if i == i[::-1]:
        b.append(i)
print(b)        

##################################################

a=["apple", "banana", "apple", "cherry"]
for i in a :
    a.count(i)


