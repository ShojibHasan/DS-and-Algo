def outer_function(x): # This is the outer function
    def inner_function(y): # This is the inner function
        print(f"Outer function argument: {x}")
        print(f"Inner function argument: {y}")
        return x + y     # inner_function can access 'x' from the outer_function
    return inner_function  # Return the inner function

# Now let's use the outer function to create a closure
closure_example = outer_function(10)

# We can now use the closure to add 10 to any number
result = closure_example(5)  # This will return 15
print(result)
