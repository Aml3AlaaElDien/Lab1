def reverse_string(string):

    reversed_string = string[::-1]
    return reversed_string

Input = input('Please insert your string: ')
reversed_result = reverse_string(Input)
print('The reversed string is: ', reversed_result)
