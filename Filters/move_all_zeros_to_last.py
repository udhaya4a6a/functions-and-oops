nums=[1,0,2,0,3]
nums.sort(key=lambda x:x==0)
print(nums)

#sort(key=...)  →  key runs first, sorting happens on key value

#lambda x: x==0
#False → 0 (non-zero goes front)
#True  → 1 (zero goes back)
#[(value, key value)]
#[(1,0), (0,1), (2,0), (0,1), (3,0)]


#sort() → in-place → returns None
#sorted() → returns new list

#Sorting Based on Key Value

#Python sorts by the key value:

#All 0 keys first → non-zeros

#All 1 keys later → zeros

#Python’s sort is STABLE 🧠

#Elements with the same key keep their original order

#So:

#[1, 2, 3] keep their order

#[0, 0] keep their order
