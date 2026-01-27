TOTAL_TICKETS = 20
MAX_PER_BUYER = 4

def sell_loop(total_tickets, max_per_buyer):
    tickets_sold = 0
    tickets_available = total_tickets
    customers = 0
    while tickets_sold < total_tickets:
        tickets_user_bought = user_tickets(tickets_available, max_per_buyer)
        tickets_sold += tickets_user_bought
        tickets_available -= tickets_user_bought
        customers += 1
    print(f"All {total_tickets} have been sold to a total of {customers} customers.")

def user_tickets(tickets_available, max_per_buyer):
    print(f"{tickets_available} tickets available, max {max_per_buyer} per buyer.")
    tickets_desired = int(input(f"How many tickets do you want to purchase? "))
    while (tickets_desired > max_per_buyer) or (tickets_desired > tickets_available):
        tickets_desired = int(input(f"Please enter a valid number of tickets: "))
    return tickets_desired

def main():
    sell_loop(TOTAL_TICKETS, MAX_PER_BUYER)

if __name__ == "__main__":
    main()