def f(x,y):
    if y==0:
        return x
    return f(y,x%y)

print( f(60, 48))
print (f(33,21))

#The output will be "12 , 3"

