import re

def main():
    # Creates a fancy dictionary menu like the one in Chapter 4
    menu = {'phone':validate_phone, 'social':validate_social, 'zip':validate_zip}
    try:
        while True:
            choice = input('Type "phone" to validate a phone number, "social" to validate a '
                           'social security number, "zip" to validate a zip code, or anything '
                           'else to quit the program: ')
            # Calls the function keyed from the menu
            (menu[choice.casefold()])()
    # This will probably be a KeyError, but a KeyboardInterrupt is
    # possible. I just used Exception as the result is the same.
    # Erroring out is ironically the only way to gracefully exit the
    # program (I hope this is alright, but please let me know if it's
    # not good practice).
    except Exception:
        print("Quitting program.")

# The validate_phone() function validates input from the user for phone
# number formatting.
def validate_phone():
    # This regex expression checks for phone number formatting, using
    # character sets for spacing between numbers, numeric quantifiers
    # for numbers, and the special characters ^ and $ to prevent counting
    # "111-111-1111111" as a valid phone number. The following functions'
    # patterns work very similarly, only differing in numbers and position.
    phone_pattern = r'^\d{3}[- ]?\d{3}[- ]?\d{4}$'
    phone = input('Enter a phone number in the format ###-###-####: ')

    # If user input matches the regex pattern, it is valid.
    if re.match(phone_pattern, phone):
        print(f'{phone} is a valid phone number.')
    else:
        print('Invalid phone number.')

# The validate_social() function validates input from the user for social
# security number formatting.
def validate_social():
    social_pattern = r'^\d{3}[- ]?\d{2}[- ]?\d{4}$'
    social = input('Enter a social security number in the format ###-##-####: ')

    if re.match(social_pattern, social):
        print(f'{social} is a valid social security number.')
    else:
        print('Invalid social security number.')

# The validate_zip() function validates input from the user for zip code formatting.
def validate_zip():
    zip_pattern1 = r'^\d{5}[- ]?\d{4}$'
    zip_pattern2 = r'^\d{5}$'
    zip = input('Enter a zip code in the format #####-####: ')

    if re.match(zip_pattern1, zip):
        print(f'{zip} is a valid zip code.')
    elif re.match(zip_pattern2, zip):
        print(f'{zip} is a valid zip code.')
    else:
        print('Invalid zip code.')

if __name__ == "__main__":
    main()