#Convert list of strings to integers using map() and int() function
str_numbers=['1','2','3','4','5']
int_numbers=list(map(int , str_numbers)) #int is a built-in function that converts string to integer(type casting)
print(int_numbers)  #Output: [1, 2, 3, 4, 5]