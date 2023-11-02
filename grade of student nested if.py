#input variable for mark sheet
no = int(input('class       : '))
name = input('Name of the student : ')
marks = int(input('Max.Marks :'))
#input values for subject
s1=int(input('Enter the mark for Language subject : '))
s2=int(input('Enter the mark for English subject : '))
s3=int(input('Enter the mark for Mathematics subject : '))
s4=int(input('Enter the mark for Physics subject : '))
s5=int(input('Enter the mark for Chemistry subject : '))
s6=int(input('Enter the mark for Biology subject : '))

#Condition checking
total = s1+s2+s3+s4+s5+s6
avg = round(total/6)

if(avg >= 81 and avg <= 100):
    grade = 'distinction'
else:
    if(avg >= 61 and avg <= 80):
        grade = 'first class'
    else:
        
        if(avg>=51 and avg <= 40):
            grade = 'second class'
        else:
            if(avg>41 and avg <=50):
                grade = 'third class'                
            else:
                grade = 'Fail'
                
#print the mark sheet
print('\n')
print(' **************JUSS International school*************')
print(' ***************Thevar Street, Ayapakkam*************')
print(' ******************Chennai-600 077*******************')
print('\n')
print('            Subject             Marks')
print('            -------             -----')
print('            Language        :  ',s1)
print('            English         :  ',s2)
print('            Mathematics     :  ',s3)
print('            Physics         :  ',s4)
print('            Chemistry       :  ',s5)
print('            Biology         :  ',s6)
print('\n')
print('****************************************************')
print('            Total           : ',total)
print('****************************************************')
print('            Average         : ',avg )
print('****************************************************')
print('            GRADE           : ', grade)
print('****************************************************')
if(grade == 'Fail'):
    print('Sorry! ' + name + ' - better luck next time. Try hard to get through')
else:
    print(  ' hearty congratulations ' + name + ' for your bright future”')
print('****************************************************')

    
