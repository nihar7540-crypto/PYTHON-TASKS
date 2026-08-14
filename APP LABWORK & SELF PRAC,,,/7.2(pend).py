def fact(n):
        if n<=1:
            return 1
        return n * fact(n-1)
print(fact(10))


def fibo(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        return fibo(n-1) + fibo(n-2)
for i in range(10):
    print(fibo(i))


b=""
def rev(a):
    global b
    if len(a)==0:
        return 
    b+=a[-1]
    a=a[:-1]
    rev(a)
s="helo"
rev(s)
print(b)

b = ""
def rev(a):
    global b
    if len(a) == 0:
        return
    b += a[-1]
    a = a[:-1]
    rev(a)
s = input("enter string : ")
rev(s)
if b==s:
    print("palindrome ")
else:
    print ("not a palindrome")