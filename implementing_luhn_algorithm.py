#The Luhn Algorithm algorithm is a formula to validate a variety of identification numbers.#
#Start by declaring a function called main, this will serve as the entry point of the program. Use the pass keyword to avoid an error.#
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    #here using str.maketrans to create a translation table that removes hyphens and spaces from the card number.#
    #then using translate method to apply this translation to the card number.#

    print(translated_card_number)

main()
#The main function is called to execute the program. It will print the card number without hyphens or spaces.#

    
