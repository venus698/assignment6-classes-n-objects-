"""#Question 1
dict={}
for i in range(1,5):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict[key]=value
print(dict)"""

#Question 2
a={}
b={}
for i in range(1,3):
    b={}
    name=input("Enter the name:")
    for j in range(1,3):
        subject=input("Enter subject:")
        marks=int(input("Enter marks:"))
        b[subject]=marks
    a[name]=b
print(a)
student=input("Enter the students name whose marks we want to see:")
print(a[student])
