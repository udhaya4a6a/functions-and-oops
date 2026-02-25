#lambda function with map()
#map() applies a function to each element and collects the returned values.
#Using lambda function inside map()
#Squaring each number in the list
numbers=[1,2,3,4,5,6,7]  
print(list(map(lambda x:x**2 , numbers)))