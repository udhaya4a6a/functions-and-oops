#Calculate final price with GST for items above ₹1000
prices = [500, 1200, 800, 2000]
result=list(map(lambda x:x+(x*0.18) , filter(lambda x:x>1000 , prices)))
print(result)