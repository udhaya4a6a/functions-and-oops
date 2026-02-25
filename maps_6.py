#Add GST (18%) to prices
prices = [1000, 2000, 500]
result=list(map(lambda x:( (x)+(x*0.18) ) , prices))
print(result)