#condition checking skipping the items - 7,13,17,21
for i in range (1,28,1):
    if(i==7):
        continue
    if(i==13):
        continue
    if(i==17):
        continue
    if(i==21):
        continue
    if(i%2)==0:
        print ('Veg',i)
    else:
        print('Non',i)
    
