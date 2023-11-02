#celcius - fahrenheit conversion between 1 to 40
print('Celcius\tFahrenheit')
for i in range (1,40,1):
    fah = (i+32)*(9/5)
    i += 1
    print(i,'\t',fah)
