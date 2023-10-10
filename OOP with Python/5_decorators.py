# inner function basics
def outer(msg):
    print('this is outer function')
    
    def inner() :
        print('this is inner function')
        print(msg)
    
    return inner
#  return inner() dile bar bar return korte thakbe, so first bar right dibe, 2nd time dibe none, erpor stop

f = outer("sarica faiza")
print(f)
# to execute the inner function
f()



# decorator
def decorator(func) :
    print("this is decorator func")

    def wrapper() :
        print(func.__name__)
        print("helloooooooooo....!")
        return func()
    return wrapper

@decorator
def print_func() :
    print("running decorator....")

print_func()

# funct = decorator(print_func)
# funct()
