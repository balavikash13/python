#assigning input for opening bank account
name = input('First name                   : ')
last = input('Last name                    : ')
dob= str(input('Date of birth              :'))
Acc = input('Saving /Current account       :')
mobile = int(input('Mobile no#             :'))
gender = input('Gender                     :')
marital = input('Married/Unmarried         :')
aadhar= input('Aadhar proof                :')
pan = input('Pancard proof                 :')
address = input('Residental proof          : ')
occ = input('Occupation                    : ')
photo = input('Photo copy                  :')
#condition checking
if(aadhar == 'uploaded'):
    if(pan == 'uploaded'):
        if(address == 'uploaded'):
            if(photo == 'uploaded'):
                application = 'submitted!'
            else:
                application = 'Failed to upload the photo'
        else:
            application = 'Failed to upload the address proof'
    else:
        application = 'Failed to upload the pan card proof'
else:
    application =    'Failed to upload the Aadhar proof'
#print the application form!!
print('\n')
print('************************Muthumariyamman Indain Bank****************')
print('***************************Los Angeles,USA*************************')
print('\n')
print('                                                     *************')
print('First name           : '+name+    '                  *           *')   
print('Last name            : '+last+    '                  *'+photo+'  *')
print('D.O.B                : '+dob+     '                  *           *')
print('Gender               : '+gender+  '                  *           *')
print('Marital              : '+marital+ '                  *************')
print('Account type         : ',Acc)
print('Aadhar no#           : ', aadhar)
print('Pan no#              : ', pan)
print('Residental address   : ',address)
print('Occupation           : ', occ)
print('\n')
print('**************************************************************')
print('application status   : ',application)
print('\n')
print('**************************************************************')
if(application == 'submitted!'):
    print(name, 'Thank you, your application will processed!!!')
else:
    print('pls upload the correct document')

print('**************************************************************')

