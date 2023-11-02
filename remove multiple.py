num = [12,34,56,23,45,12,34,67,89,90,12,56,12]
dep = int(input('enter the value: '))
for i in num:
    if (i==dep):
        num.remove(dep)
print('Values of 12 is removed',num)
    
