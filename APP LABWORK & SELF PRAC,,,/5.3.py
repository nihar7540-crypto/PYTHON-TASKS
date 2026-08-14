a={23123,123413,1321,312}
a.add(6)
a.discard(3)
print(2 in a)
print(a)

##################################################################

a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

##################################################################

a={"name":"Alice","Age":20,"grade":"A"}
for i in a:
    print(i,"=",a[i])
a["city"]="Delhi"
a["Age"]=21
del a["grade"]
print(a)

##################################################################

keys=['id','name','email']
value=[101,'Bob','bob@example.com']
newd={}
for i in range(len(keys)):
    newd[keys[i]]=value[i]
print(newd)

##################################################################

a="123"
print(int(a))
b=[1,2,3]
print(tuple(b))
c=(1,2,3)
print(list(c))
d=[('1','A'),('2','B')]
c=dict(d)

##################################################################

del c['2']
print(c)

##################################################################