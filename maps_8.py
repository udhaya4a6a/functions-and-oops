#Remove spaces from strings
data = [" hello ", " python ", " map "]
result=list(map(lambda x: x.strip() , data))
print(result)