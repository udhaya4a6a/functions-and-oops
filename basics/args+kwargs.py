def print_numbers(*args,**kwargs):
    for i in args:
        print(f"positional argument: {i}")
    for key,value in kwargs.items():
                print(f"{key}:{value}")    
print_numbers(1,2,3,4,5,"END",Name="Udhaya",Age="20",height="178cm",weight="73kg")    