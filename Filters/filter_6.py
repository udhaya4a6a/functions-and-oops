#Filter valid emails
data = ["test@gmail.com", "123", "hello@yahoo.com"]
result=list(filter(lambda x: ('@') in x , data))
print(result)