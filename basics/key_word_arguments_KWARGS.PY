# KEY WORD ARGUMENTS - **kwargs
def print_details(**kwargs): #keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Udhaya", age=21, city="Chennai")