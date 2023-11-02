#Empty list and values provide during runtime
list =[]

num = int(input('Enter the values : '))
for i in range(0,num,1):
    item = input()
    list.append(item)        
print(list)

list1=[]
num1 = int(input('Enter the values : '))
for i in range(0,num1,1):
    item1 = input()
    list1.insert(i,item1)
print(list1)
    

