lname=input("enter your last name: ")
fname=input("enter your first name: ")
print(f"Hello ,{lname},{fname}!")

########################################################

item=input("enter the name of the item :")
price=input("entr the price of the item :")
a=f"the price of {item} is {price} dollars"
print(a)
b=a.split()
b[3]="apple"
b[5]="5.50"
print(" ".join(b))

#######################################################

str1=input("enter a string :")
b=str1[::-1]
if b==str1:
    print("string is palindrme")
else:
    print("string is not plaindrome")    

#######################################################

str1=input("enter a string : ")
print(str1.lower())
print(str1.upper())
print(str1.title())

#######################################################

str1="Machine Learning and AI are trending"
a=str1.split()
print(a)
a[3]="Artificial Intelligence"
print(" ".join(a))
print(str1.replace("AI","Artificial Intelligence"))

#######################################################

str1="data data maining and big data"
str2=str1.title()
print(str2.count("Data"))

#######################################################

strlst=["Python","is","Awesome"]
a=" ".join(strlst)
print(a)

#######################################################

str1="""Hello World ,This is Python 
and Hello Python ,This is World"""
a=str1.splitlines()
for i in a:
    print(i)


########################################################

str1="Data123#Science!"
a=list(str1)
print(a)
for i in a:
    if i.isalpha():
        print(i,end="")
    else:
        continue  

########################################################

str1="python"
print(str1[::-1])
