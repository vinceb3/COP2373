import random

# Creates lists for the ranks and suits of a standard 52-card deck
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

# The Deck() class creates instances of a deck of any size, chosen by the user.
# The argument "52" results in a standard card deck.
class Deck():

    def __init__(self, size):
        self.card_list = [n for n in range(size)]
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")
        return self.card_list.pop()

def poker():
    # Create a standard card deck
    deck = Deck(52)

    # Deal the user 5 cards and it them to their hand
    hand = [deck.deal() for n in range(5)]
    print_hand(hand)

    # The while True block will loop until it gets good input
    while True:
        try:
            discarded = input("What cards would you like to discard? (type any integers "
                            "1 through 5 spaced out by commas: e.g., '1, 3, 5') ")

            # Split the input, strip it of the comma (instead of just
            # splitting by the delimiter ", " in case the user didn't
            # use a space, and makes it an int.
            discarded = [int(n.strip()) for n in discarded.split(",")]

            # Checks if all of the numbers are within the standard range; the
            # loop will break if they are
            if all(1 <= n <= 5 for n in discarded):
                break
            print("Error: Those cards don't exist! Please try again.")
        except Exception:
            print("Error: Incorrect format, please try again.")

    # Sort and reverse the list to pop the correct cards
    discarded.sort()
    discarded = discarded[::-1]

    for num_card in discarded:
        discard = hand.pop(num_card - 1)

    # Deal cards for every discarded card
    hand += [deck.deal() for n in range(len(discarded))]

    print_hand(hand)

# The print_hand() function accepts a poker hand (in the form of a list) as
# an argument. A for loop is used to iterate through the list (enumerate() is
# used to give each card a designated number, 1-5. Integer division and
# modulus by 13 are used with the global lists to assign values to each
# card ID.
def print_hand(hand):
    for n, card_number in enumerate(hand):
        print(f"{n + 1}. {rank[card_number % 13]} of {suit[card_number // 13]}")

def main():
    poker()

if __name__ == "__main__":
    main()