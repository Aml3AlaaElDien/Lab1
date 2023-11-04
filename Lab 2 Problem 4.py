# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


N = int (input('Please enter a number: '))
S = 0
x = int(input('enter a value '))
if x < 0:
    print('The number is negative.')
else:
    for i in range(1, N + 1, 1):
        S = S + x
    print(S)




