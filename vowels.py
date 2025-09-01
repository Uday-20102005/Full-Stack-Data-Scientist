x=input('enter a sentence:')
vowels=['a','e','i','o','u','A','E','I','O','U']
vowels_count=0
con_count=0

for i in x:
    if i in vowels:
        vowels_count+=1
    else:
        con_count+=1

print(vowels_count)
print(con_count)