#map() applies a function to each element and collects the returned values.
numbers=[1,2,3,4,5,6,7]  
def square(x):
    return(x**2)
result=map(square ,numbers)
print(list(result))