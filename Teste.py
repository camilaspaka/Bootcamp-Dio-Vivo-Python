def capitalize_decorator(func): 
    def wrapper(): 
        return func().upper() 
    return wrapper 

@capitalize_decorator 
def greet(): 
    return "hello" 

print(greet())