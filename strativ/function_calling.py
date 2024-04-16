def before_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling function: {func.__name__}")
        return func(*args, **kwargs)
    print(f"Wrapper: {wrapper.__name__}")
    return wrapper


@before_function_call
def main():
    print("Inside main function")

main()
