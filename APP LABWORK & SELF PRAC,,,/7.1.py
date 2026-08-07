l=[]
for i in range(5):
    a=int(input("enter element for list : "))
    l.append(a)
print(len(l))
print(max(l))
print(sorted(l))
print(sum(l))   
print(type(l)) 

#####################################################################

def fact(n):
    factt=1
    for i in range(n):
        factt*=i+1
    return factt
print(fact(3))        

#####################################################################

def sq(l):
    sqlst=[i**2 for i in l]
    return sqlst
list=[int(input("enter the elements for the list: ")) for i in range(5)]
print(sq(list))


#####################################################################

def freq(s):
    fdict={}
    for i in s:
        b=s.count(i)
        fdict[i]=b
    return fdict
a=input("enter the elements for the string: ") 
print(freq(a))

#####################################################################

def cub(l):
    cublst=[i**3 for i in l]
    return cublst
list=[int(input("enter the elements for the list: ")) for i in range(5)]
print(cub(list))

#####################################################################

def nums(*args):
    sum=0
    prod=1
    for i in args:
        sum+=i
        prod*=i
    print("sum is",sum ,"product is",prod)
nums(6,9,9,9)

#####################################################################

def stud(*args):
    if len(args) != 0:
        for i in args:
            print(i)
    else:
        print("empty")        
studlst = []
for i in range(5):
    a = input("enter the name of student: ")
    studlst.append(a)
b = tuple(studlst)
stud(*b) 

#####################################################################

def filter(*args):
    strings=[]
    nums=[]
    for i in args:
        if type(i)==str:
            strings.append(i)
        else:
            nums.append(i)
    strtpl=tuple(strings)
    numtpl=tuple(nums)
    return strtpl,numtpl

print(filter(10,"apple",100,"ahmedabad",98))

#####################################################################

def info(**kwargs):
    print("name is",kwargs[name])
    print("age is",kwargs[age])
    print("city is",kwargs[city])

info(name="rajesh",age=10,city="ahmedabad")

#####################################################################

def prod(**kwargs):
    p=kwargs["price"]
    q=kwargs["quantity"]
    totalp=p*q
    return totalp
print(prod(name="dant kanti",price=100,quantity=200))
print(prod(name="5 star",price=344,quantity=10))
print(prod(name="chavanprash",price=52,quantity=230))
print(prod(name="agarbatti",price=120,quantity=50))


#####################################################################

def checkemp(**kwargs):
    missingfld = []
    if "name" not in kwargs:
        missingfld.append("name")
    if "department" not in kwargs:
        missingfld.append("department")
    if "salary" not in kwargs:
        missingfld.append("salary")

    if len(missingfld) > 0:
        print("warning! the following fields are missing:")
        for i in missingfld:
            print("-", i)
    else:
        print("employee accepted:", kwargs)
checkemp(name="nihar", age=19)
checkemp(name="raj", age=20, department="DS", salary="16 lpa")


#####################################################################

def arofc(a):
    '''calculate the total surface area of the circle 
       args:take the integer value of radius of the circle 
       
       return value
       --------
       float:calculated area of the circle
       '''
    a=3.14*(a**2)
    return a
b=int(input("enter the radius: "))
print(arofc(b))
print(arofc.__doc__)

#####################################################################

def fibo(n):
    '''takes the number of terms as integer input and give the fibonacci sequence of that no of terms
       args:takes the integer value of number of terms
       
       return value
       ------------
       integer:fibonacci series'''
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
terms =int(input("enter the no of terms"))
for i in range(terms):
    print(fibo(i))

