# arr=[]
# for i in range(3):
#     lst=[]
#     for j in range(3):
#         b=int(input(f"enter the element for column {j+1} and row {i+1}: "))
#         lst.append(b)
#     arr.append(lst)
# for i in arr:
#     for j in i:
#         print(j,end=" ")
#     print()

arr=[]
for i in range(2):
    lst=[]
    for j in range(3):
        b=int(input(f"enter the element for row {j+1} and column {i+1}: "))
        lst.append(b)
    arr.append(lst)
for i in arr:
    for j in i:
        print(i,end=" ")
    print()
