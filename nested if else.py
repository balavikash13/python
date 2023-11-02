#input variable for mark sheet
no = int(input('Enter the class: '))
teacher = input('Enter name of the teacher: ')
name = input('Enter the student name: ')
rollno = int(input('Enter the roll no# :'))
#input values for subject
s1=int(input('Enter the mark for Tamil subject : '))
s2=int(input('Enter the mark for English subject : '))
s3=int(input('Enter the mark for Mathematics subject : '))
s4=int(input('Enter the mark for Science subject : '))
s5=int(input('Enter the mark for Social subject : '))

#Condition checking
if(s1>40):
    if(s2>40):
        if(s3>40):
            if(s4>40):
                if(s5>40):
                    res = 'Pass'
                else:
                    res ='Fail in social'
            else:
                res = 'Fail in science'
        else:
            res = 'Fail in maths'
    else:
        res = 'Fail in english'
else:
    res = 'Fail in tamil'

#print the mark sheet
print('\n')
print('   **************DUBAI INTERNATIONAL SCHOOL*************')
print(' *********Dubai main road, dubai kuruku sandhu************')
print('   ******************Dubai-600021***********************')
print('\n')
print('            Subject             Marks')
print('            -------             -----')
print('            Tamil           :  ',s1)
print('            English         :  ',s2)
print('            Mathematics     :  ',s3)
print('            Science         :  ',s4)
print('            Social          :  ',s5)
print('\n')
print('             Result  : ',res)
if(res == 'Pass'):
    print(          name,'Congrats you are passed in examination')
else:
    print(          name,'Sorry you are not pass in exam and better luck next time!')
