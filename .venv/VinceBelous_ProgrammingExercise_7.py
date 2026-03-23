import re

# The matching() formula asks the user for input, creates a regex pattern,
# and finds matches using the two. It return a list of the matches.
def matching():
    user_input = input("Enter a paragraph: ")

    # [0-9A-Z] matches the first letter/number of a sentence. .*? matches
    # any number of characters (non-greedily). [.!?] matches the end
    # punctuation of the sentence. (?= [A-Z]|$) looks ahead for the
    # beginning of a new sentence or the end of the line/string. P.S.
    # This might get messy with titles like Mr. and Mrs. but I think
    # that's outside the scope of this assignment. Please forgive me
    # if I'm wrong, though.
    paragraph_pat = r"[0-9A-Z].*?[.!?](?= [A-Z]|$)"

    # Creates a list of all the sentences in user_input. The
    # re.DOTALL flag lets "." characters see newlines as individual
    # characters, and the re.MULTILINE flag lets "$" characters match
    # newlines and ends of strings.
    matches = re.findall(paragraph_pat, user_input, flags=re.DOTALL | re.MULTILINE)

    # Return the list of matched groups.
    return matches

# The output() function prints the individual sentences and the number of
# sentences to the user.
def output(matches):
    # This loop prints out the sentences. It uses the enumerate()
    # function to give each sentence a number, originally its index
    # but adjusted by the assignment num += 1 to be sentence number.
    for num, match in enumerate(matches):
        num += 1
        print(f"Sentence {num}: {match}")

    print(f"There are {len(matches)} sentences.")

def main():
    output(matching())

if __name__ == "__main__":
    main()