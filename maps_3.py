#Convert list of strings to uppercase using map() and lambda function
words = ["python", "django", "api"]
print(list(map(lambda x : x.upper() , words))) #or print(list(map(str.upper , words)))
#Output: ['PYTHON', 'DJANGO', 'API']