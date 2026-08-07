arr=[1,4,456,32,45,76,45,75]
for i in arr :
    print(i)

###########################################################

sum=0
for i in arr :
    sum+=i
    print(sum)

###########################################################

a=int(input("enter the element to insert: "))
b=int(input("enter the index to add there: "))
arr.insert(b-1,a)
print (arr)

###########################################################

a=int(input("enter the element to remove from array: "))
index=arr.index(a)
del arr[index]
print(arr)

###########################################################

print(arr)
a=int(input("enter the number to update: "))
b=int(input("enter the new number:"))
c=arr.index(a)
arr[c]=b
print(arr)

###########################################################

def findind(l):
    """
    Searches a list for a user-specified integer.
    Parameters:
    l (list): The list to search.
    Returns:
    int: The index of the element, or a message if not found.
    """
    a = int(input("Enter the element to search: "))
    for i in range(len(l)):  
        if a == l[i]:       
            return i
    return "element not found"                
arr = [1, 4, 456, 32, 45, 76, 45, 75]
print(findind(arr))

###########################################################

arr2=[1,2,4,54,5,6,55676,]
print(arr+arr2)


