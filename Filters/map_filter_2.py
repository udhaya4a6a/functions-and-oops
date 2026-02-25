#Convert names starting with 'a' to uppercase
names = ["apple", "banana", "avocado", "grape"]
result=list(map(lambda x:x.upper() , filter(lambda x: x.startswith ('a'), names)))
print(result)