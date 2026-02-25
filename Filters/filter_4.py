#Filter names starting with 'a'
names = ["apple", "banana", "avocado", "grape"]
def start_with_a(dummy):
    return dummy.startswith('a')
print(list(filter(start_with_a , names)))