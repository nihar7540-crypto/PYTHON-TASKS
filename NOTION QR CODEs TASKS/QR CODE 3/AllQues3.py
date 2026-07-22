# str1="  Hello World "
# a=str1.strip()
# print(a.lower())

# ################################################

# a="hello world"
# print(a.title())

# ################################################

# a = "hello!!! world???"
# text = ""
# for i in a:
#     if i.isalpha() or i== " ":
#         text =text + i
# print(text)

        

################################################

# a="a1b2c3"
# b=a.split()
# c=[]
# for i in a:
#     if i.isdigit():
#         c.append(i)
#     else:
#         continue
# print("".join(c))    
        
 

# ################################################

# a="a1b2c3"
# b=a.split()
# c=[]
# for i in a:
#     if i.isalpha():
#         c.append(i)
#     else:
#         continue
# print("".join(c))   

# ################################################

# a="I love Python"
# b=a.split()
# b.reverse()
# c=" ".join(b)
# print(c)

# ################################################

# a="this is is a test test"
# b=a.split()
# for i in b:
#     if b.count(i)==2:
#         b.remove(i)
# print(" ".join(b))

# ################################################

# email = "test@gmail.com"
# is_valid = email.count("@") == 1 and email.endswith(".com")
# print(is_valid)  

# ##################################################

# a="9876543210"
# b=list(a)
# b[3:8]="*****"

# print("".join(b))

# ##################################################

# a="Hello World Python"
# b=a.replace(" ","_")
# c=b.lower()
# print(c)

# ###################################################

# a=input("enter string: ")
# b=a.split()
# for i in b:
#     char=list(i)
#     char.remove(char[0]) 
#     char.remove(char[-1])
#     z=str("".join(char))
#     print(z,end=" ")

###################################################

# a = "I love Python programming"
# b = a.split()
# c=max(b)
# print(c)

###################################################

# a = "Hello, world! Python is great."
# words = a.split() 
# word_count = 0
# for item in words:
#     has_letter = False
#     for char in item:
#         if char.isalpha():
#             has_letter = True
#     if has_letter:
#         word_count = word_count + 1
# print("Word Count:", word_count)

###################################################

# a="nurses run"
# b=a.replace(" ","")
# revstr=b[::-1]
# if b==revstr:
#     print("palindrome")
# else:
#     print("not palindorme")    

###################################################

a="HeLLo"
b=list(a)
for i in b:
    if i.isupper():
        i.upper()
    elif i.islower():
        i.lower()
print("".join(b))            
    

    
    
