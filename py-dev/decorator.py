'''
decorator in python is used for adding some additional behaviour in a existing function without modifying the implementation of the original function.

basically it is a wrapper which will wrap the original function and implement something before it or after it according to the usercases.

functions are objects in python.

'''
def a_new_decorator(function_to_be_decorated):
    def wrapper_for_original_function():
        print("before the original function") 
        print(function_to_be_decorated())
        print("after the original function")    
    return wrapper_for_original_function

# def a_standalone_function():
#     return "this is a standalone function."


# returned_function = a_new_decorator(a_standalone_function)
# returned_function()

# a_standalone_function = a_new_decorator(a_standalone_function) overriding.
# a_standalone_function()

# recommended
@a_new_decorator
def a_standalone_function():
    return "this is a standalone function."

a_standalone_function()

# adding @a_new_decorator is equivalent to => a_standalone_function = a_new_decorator(a_standalone_function)

# un-decorating a function is "Hard"