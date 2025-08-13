#In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.#

#List comprehension is a short and readable way to create a new list in Python by doing three things in one line:
#1.Looping through something (like a list, string, or range)
#2.Optionally filtering items
#3.Transforming each item into a new value

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = ['_' + char.lower() if char.upper() else char for char in pascal_or_camel_cased_string]
    
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()