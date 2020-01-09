# I am a module!

# Here's a variable
about_pi = 3.14

# Here's the definition of myfunc
def myfunc(arg1, arg2):
    print("I am a function in a module! Here are my arguments:")
    print(arg1)
    print(arg2)
    print("I am returning my first argument now!")
    return(arg1)

# Here's another function
def myfunc1(arg1):
    print("I only take one argument. It is:")
    print(arg1)
    print("I also don't return anything. Bye!")

# Yet another function
def myfunc2(arg1, arg2='cheese', arg3='sandwich'):
    print("I take one mandatory argument, and two optional ones.")
    print("The mandatory argument is:")
    print(arg1)
    print("The optional arguments are:")
    print(arg2)
    print(arg3)
