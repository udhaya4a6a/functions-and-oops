#reverse_string_using_recursion
def reverse_string(s):
    """
    Docstring for reverse_string
    
    :param s: Description
    """
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string (s[:-1])
print(reverse_string("udhaya") )  # Example usage       
    
