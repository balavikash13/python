#program for preparing a table to have celcius - fahrenheit conversion between 1 to 40

cel = 1
print('celcius\tfahrenheit')
while(cel<30):
    fah = (cel + 32)* (9/5)
    cel = cel + 1
print(cel,'\t',fah)
