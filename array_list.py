a = [1, 2, 3]
b = ['d', 'f', 's']

print(a, b)
print(a[0])
# slicing
print(a[0 : 2]) 
# -1 mane last index, -2 mane 2nd last
print(a[-1])
print(a[0 : -1])

# make double 
a = 2 * a
print(a)

# delete 
del a[5]
print(a)

# try-except
for i in range(0, 5) :
    try :
        print(b[i], a[i])
    except :
        print("index out of bounds")
