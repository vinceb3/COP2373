# Establish global constants. These values will be manipulated by
# functions, but the values of these variables themselves will stay
# the same.
TOTAL_TICKETS = 10
MAX_PER_BUYER = 4

# The sell_loop() function contains the core of the program, a while
# loop that engages another function to ask the user how many tickets
# they want and then registers that data, applying it to accumulators.
# It accepts two arguments that correspond to the two global constants.
def sell_loop(total_tickets, max_per_buyer):

    # Initializes variables
    tickets_sold = 0
    tickets_left = total_tickets
    customers = 0

    # While not all of the tickets are sold yet, sell tickets.
    while tickets_sold < total_tickets:
        # Calls the user_tickets() function, which returns the number
        # of desired tickets to the tickets_user_bought variable.
        tickets_user_bought = user_tickets(tickets_left, max_per_buyer)

        # Accumulator changes
        tickets_sold += tickets_user_bought
        tickets_left -= tickets_user_bought
        customers += 1

    # Tells the user how many tickets and customers there were.
    print(f"All {total_tickets} have been sold to a total of {customers} "
          f"customers.")

# The user_tickets() function prompts the user for how many tickets
# they want. Once a valid number is entered, that value is returned.
# This function accepts two arguments, one corresponding to the
# MAX_PER_BUYER global constant, and the other the number of
# tickets left.
def user_tickets(tickets_available, max_per_buyer):

    # Tells the user how many tickets are available and how many they
    # can buy.
    print(f"{tickets_available} tickets available, max {max_per_buyer} per "
          f"buyer.")

    # This while True block will break once no ValueError input occurs.
    while True:
        # This try-except block tests the user input for values that
        # will cause the int() function to error out, like decimals
        # and words.
        try:
            # Gets the number of tickets desired from the user.
            tickets_desired = int(input(f"Enter an integer number for how many"
                                        f" tickets you would like to purchase: "))
            break
        except ValueError:
            print("ERROR: Only integers (e.g. 3, 11) are accepted. Please try again.")
    # Tests the user's value for validity. It cannot be greater than
    # the number of tickets available or maximum tickets per buyer.
    while ((tickets_desired > max_per_buyer) or
          (tickets_desired > tickets_available)):
        tickets_desired = int(input(f"Please enter a valid integer: "))
    return tickets_desired

def main():

    # Calls the sell_loop() function with the two global constants as
    # arguments. The sell_loop() function calls the user_tickets()
    # function to get user input.
    sell_loop(TOTAL_TICKETS, MAX_PER_BUYER)

if __name__ == "__main__":
    main()