#map with multiple itterables
#Adding corresponding elements of two lists
num1=[1,2,3]
num2=[4,5,6]
result=list(map(lambda x,y : x+y , num1,num2))
print(result) #Output: [5, 7, 9]