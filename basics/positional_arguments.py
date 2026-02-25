#normal multiple parameter method
def print_num(a,b,c,d): #muliple parameters
    print(a,b,c,d)
print_num(10,21.7,"hello",1)    

#*************************************************************************************

#variable length Arguement -> positional and keyword arguments

#*************************************************************************************

def print_numbers(*args): #variable length positional arguments
    for i in args:
        print(i)
    print()
print_numbers(10,20,30,40,57.12344,"vanakam")    