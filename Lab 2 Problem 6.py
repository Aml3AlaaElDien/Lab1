# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


N_arr = input ('Enter numbers: ')
even_sum = 0
odd_sum = 0
for i in N_arr.split():
    if int(i) % 2 == 0:
     even_sum = even_sum + int(i)
    else:
     odd_sum = odd_sum + int(i)
print ('even sum= ', even_sum)
print ('odd sum' , odd_sum)

