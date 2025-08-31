#Write an application to pre-sell a limited number of cinema tickets.
#Each buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
#Prompt the user for the desired number of tickets and then display the number
#of remaining tickets after their purchase. Repeat until all tickets have been sold.
#Then display the total number of buyers.

#Function to achieve the number of tickets the buyer wants to purchase
def get_ticket_request(tickets_remaining):
    while True:
        try:
            requested = int(input(f"\nHow many tickets would you like to purchase? (The Max is 4, {tickets_remaining} remaining): "))
            if requested < 1:
                print("You have to buy at least 1 ticket please.")
            elif requested > 4:
                print("You can only buy up to 4 tickets, try again please.")
            elif requested > tickets_remaining:
                print(f"There is only {tickets_remaining} ticket/tickets left. Please purchase a smaller amount.")
            else:
                return requested
        except ValueError:
            print("Please enter a valid number, not a letter or a symbol.")

#Function to process a purchase 
def process_purchase(requested, tickets_remaining):
    tickets_remaining -= requested
    print(f"Your purchase was successful. {tickets_remaining} tickets remaining.")
    return tickets_remaining

#Program for total tickets
def main():
    total_tickets = 20
    buyers = 0  #The accumulator

    while total_tickets > 0:
        requested = get_ticket_request(total_tickets)
        total_tickets = process_purchase(requested, total_tickets)
        buyers += 1  #Counting the number of buyers

    print(f"\nAll tickets sold! Total number of buyers: {buyers}")

# Run the program
main()
