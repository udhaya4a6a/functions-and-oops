#map + filter Together (Very Common Question)
#Square only even numbers
lst=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x:x**2  , filter(lambda x:x%2==0,lst)))
print(result)