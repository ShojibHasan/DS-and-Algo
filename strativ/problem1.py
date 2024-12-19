def function1(func):
    def function2(*args, **kwargs):
        print("Starting....: ",func.__name__)
        print("Ending....")
        return func(*args, **kwargs)
        
    return function2
        

@function1
def greet(name):
    print(f"hello {name}")
    
greet("arif")