# Types of functions arguments -> Required argument(Positional Argument), Keyword argument, Default Argument
# Arbitrary Argument(*args), Arbitrary Keyword Argument (**Kwargs)  


# Required Argument

def greet(name:str, age:int):
    print(f"Hello {name}. You are {age} years old.")
greet("Rijan", 20)

# Keyword Argument
def greet(name, age):
    print(f"Hello {name}. You are {age} years old.")
greet(name="Rijan", age=43)