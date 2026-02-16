# Initializes a global constant to represent the base spam score.
SPAM_SCORE = 0.5

# Initializes a list of thirty spam words.
spam_words = ["winner", "claim", "inheritance", "cash", "free", "refinance",
              "investment", "earn", "urgent", "immediate", "account suspended",
              "unauthorized login", "final notice", "expires today",
              "while supplies last", "limited time", "verify", "update your",
              "security alert", "click the link below", "password reset",
              "confirm your", "cure", "lose weight fast", "miracle",
              "viagra", "prescription-free", "your package is",
              "delivery failed", "invoice"]

# The spam_check_loop() function holds the main program loop, deferring
# calculation to the spamalyzer() function.
def spam_check_loop(spam_score):
    # This try-except block should catch all unforeseen errors.
    try:
        # The casefold method is used to ensure that the string is
        # completely lowercase to allow for simpler checking.
        email = input("Enter an email to check for spam: ").casefold()
    except Exception as error:
        print(f"ERROR: {error}"
              f"Please restart the program and try again.")

    # Calls the spamalyzer() function and assigns the two returned
    # values to two variables.
    word_occurrences, spam_score = spamalyzer(email, spam_score)

    # This if-elif-else block prints the user's spam score.
    if spam_score > 1:
        print(f"Spam score: {spam_score:.0%}. You should probably change your email address.")
    elif spam_score > 0.7:
        print(f"Spam score: {spam_score:.0%}. This is probably a spam email.")
    else:
        print(f"Spam score: {spam_score:.0%}. This might be a spam email.")

    # If the word_occurrences dictionary is empty, tell the user.
    if not word_occurrences:
        print(f"None of the registered spam words came up.")
    else:
        print(f"The suspect word(s) and phrase(s) are...")
        # Prints the words that appearedand the number of times that
        # they appeared.
        for key, value in word_occurrences.items():
           # Titles the keys to make them uppercase.
            print(f"{key.title()}: {value} times.")

# The spamalyzer() function contains the spam calculator.
def spamalyzer(email, spam_score):
    word_occurrences = {}
    # For every possible word, check the email for a spam word. Count
    # how many times it appeared, if any. If it did appear, record it
    # in the word_occurrences dictionary and increase the spam score.
    for word in spam_words:
        times_found = email.count(word)
        if times_found >= 1:
            word_occurrences[word] = times_found
        spam_score += (times_found / 20)
    return word_occurrences, spam_score

def main():
    spam_check_loop(SPAM_SCORE)

if __name__ == "__main__":
    main()
