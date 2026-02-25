## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]
result=list(filter(lambda x:x['age']>25 , people))
print(result,end="   ")
print()