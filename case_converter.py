#In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.#

#First using loop to build the converter#
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    #.join() concatenates the list into a single string, here ''.join() means no separator is used#
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    
    return clean_snake_cased_string

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()