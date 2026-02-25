def is_palindrome(s):
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s=s.lower()
    s=s.replace(" ","")
    if s==s[::-1]:
        return True
    else:
        return False
print(is_palindrome("A man a plan a canal Panama"))  # Example usage    
print(is_palindrome("Hello"))  # Example usage