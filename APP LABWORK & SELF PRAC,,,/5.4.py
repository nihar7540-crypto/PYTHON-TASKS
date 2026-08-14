students=[{"id":101,"name":"Alice","score":85},{"id":102,"name":"Bob","score":78},{"id":103,"name":"Charlie","score":92}]
newstud={}
sum=0
for i in students:
        print(i["name"])
        scores=i["score"]
        sum+=scores
        if i["id"]==102:
            i["score"]=88
print(sum/len(students))
print()
print(students)
print()
for i in students:
        if i["name"]=="Charlie":
            students.remove(i)
print()
newid=int(input("enter the new id: ")) 
newname=input("enter new name: ")
newscore=int(input("enter the score: "))
newstud["id"]=newid 
newstud["name"]=newname
newstud["score"]=newscore   
students.append(newstud)
print(students)
print()
for i in students:
    if i["score"]>80:
        print(i["name"])
print()
scoress=[]
for i in students:
    scoress.append(i["score"])
scoress.sort()
print(scoress[::-1])
print()
maxsc=max(scoress)
for i in students:
    if i["score"]==maxsc:
        print(i)
print()
for i in students:
    if i["score"]>=90 and  i["score"]<=100:
        i["grade"]='A'
    elif i["score"]>=80 and i["score"]<90:
        i["grade"]='B'
    elif i["score"]<0 and i["score"]>100:
        print("marks not defined to give grade")
    else:
        i["grade"]='C'
    print(f"- Name: {i["name"]} | Score: {i["score"]} | Grade: {i["grade"]}")
print()
print(students)
print()
gotAgrd=0
gotBgrd=0
gotCgrd=0
for i in students:
    if i["grade"]=='A':
        gotAgrd+=1
    elif i["grade"]=='B':
        gotBgrd+=1
    elif i["grade"]=='C':
        gotCgrd+=1
    
print("students with grade A: ",gotAgrd)
print("students with grade B: ",gotBgrd)
print("students with grade C: ",gotCgrd)
print()
print("mean(scores) :",sum/len(students))
print("min(scores) :",min(scoress))
print("max(scores) :",max(scoress))
