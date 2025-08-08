#The Luhn Algorithm algorithm is a formula to validate a variety of identification numbers.#
#Start by declaring a function called main, this will serve as the entry point of the program. Use the pass keyword to avoid an error.#
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    #Reversing the card number to process it from the last digit to the first.#
    odd_digits = card_number_reversed[::2]
    #Extracting the odd indexed digits (0-based index) from the reversed card number.
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    #here using str.maketrans to create a translation table that removes hyphens and spaces from the card number.#
    #then using translate method to apply this translation to the card number.#

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
#The main function is called to execute the program.#

    
