'''
In Python, the nonlocal statement is used to
indicate that a variable in a nested function isn’t local.
It enables you to modify variables in an outer,
but non-global scope from within a nested function.

'''
def outer_function():

    outer_variable = 10

    def inner_function():

        nonlocal outer_variable

        outer_variable = 20  # Modify the variable in the enclosing scope

    inner_function()

    print("Outer variable:", outer_variable)  # Output: 20

outer_function()