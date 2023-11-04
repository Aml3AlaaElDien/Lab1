# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Vowels = ['a', 'e', 'i', 'o', 'u']
Statement = input('Enter what you want: ').lower()
counter = 0
for letter in Statement:
    if letter in Vowels:
        counter = counter +1
if counter == 0:
    print('No Vowels found')
else:
    print('There is: ', counter, 'vowel letters in the statement')
