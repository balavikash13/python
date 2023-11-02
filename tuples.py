#declare variable
stu = ('arun','akash','babu','chandra','ciran','delhi','dedhu','eshwar','farahna','hana','babu','yogi','varun','ilaya','akila')
marks= (45,56,34,65,89,32,78,45,79,80,33,67,90,65,70)
roll= [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015]
m = marks.index(min(marks))
x = marks.index(max(marks))
f = marks.count(max(marks))
print('Top scorer in class',stu[x],marks[x],roll[x])
print('Least scorer in class',stu[m],marks[m])
print('frequency of max marks',f)
roll.append(1016)
print('append',roll)
