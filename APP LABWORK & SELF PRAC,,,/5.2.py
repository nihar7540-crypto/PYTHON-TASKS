a=["apple","banana","pineapple"]
a.append("mango") #['apple', 'banana', 'pineapple', 'mango']
a.remove(a[0]) #['banana', 'pineapple', 'mango']
a.sort() #['banana', 'mango', 'pineapple']
a.reverse() #['pineapple', 'mango', 'banana']
print(a)

##########################################################

tpl2=()
for i in range(3):
    tpl=input("enter the elements for the tuple:")
    tpl2+=(tpl,)
a=list(tpl2)
b=input("enter the element you want to change with 2nd place :")
a[1]=b
print(tuple(a))

##########################################################

tpl2=()
lst=[]
for i in range(3):
    tpl=input("enter the elements for the tuple:")
    tpl2+=(tpl,)
for j in range(3):
    lst1=input("enter the elements for the list:")
    lst.append(lst1)
print(tpl2)
print(lst)
lst[0]="hello"
print(lst)
tpl[0]="hello"


##########################################################

lst1=[]
evenlst=[]
for i in range(1,20+1):
    lst1.append(i)
print(lst1)
for j in lst1:
    if j%2==0:
        evenlst.append(j)
print(evenlst)

##########################################################

a=["hello","WORLD","PyThOn"]
b=[]
for i in a:
    c=i.lower()
    b.append(c)   
print(b)




