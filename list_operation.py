#list=[1,2,3,4,5,6,7,8,9]
#print(list[0])
#$print(list[1:8:1])


list1=[]
for a in range(0,10):
    a=int(input("Entrer th number: "))
    list1.append(a)
print(list1[::])
try:
    x=int(input("Enter the starting index: "))
    y=int(input("Enter the Ending index: "))
    z=int(input("Enter the jumping values index: "))
    print(list1[x:y:z])
except:
    print("Enter the values correctly")
q=int(input("Enter the index: "))
w=int(input("Enter the another value for index: "))
list1[q]=w
print(list1)
