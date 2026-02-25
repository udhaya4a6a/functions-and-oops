def convert_temp(temp, unit):
    """Convert temperature between Celsius and Fahrenheit."""
    if unit=='C' or unit=='c':
        # Convert Celsius to Fahrenheit
        fahrenheit= (temp * 9/5) + 32
        print("Fahrenheit:", fahrenheit)
    elif unit=='F' or unit=='f':
        # Convert Fahrenheit to Celsius
        celsius= (temp - 32) * 5/9
        print("Celsius:", celsius)
    else:
        print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
# Example usage
convert_temp(float(input("enter celcius or fahrenheit Temperature:")), input("enter the unit you want to convert C/F: "))  #C for Celsius and F for Fahrenheit
    
