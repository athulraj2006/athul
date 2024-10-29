#created by athul raj
#date:29-10-24
string_input=input("enter a string:")
vowels ="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print("no of vowels in given string:",vowels_count)
