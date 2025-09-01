x = int(input('Enter a number: '))
y = str(x)
digitlen = len(y)  
sum_of_powers = 0
for i in y:
    sum_of_powers += int(i) ** digitlen  
if sum_of_powers == x:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
