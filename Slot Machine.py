import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# dictionaries containing the count of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# dictionaries containing the value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# a function to check the winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # loop over the number of lines 
    for line in range(lines):
        # get the symbol in the first column of the current line
        symbol = columns[0][line]

        # loop over each column in the slot machine
        for column in columns:
            symbol_to_check = column[line]

            # if the symbol in current column and line is not same as symbol in first column and line, break out of loop
            if symbol != symbol_to_check:
                break
        else:
            # If all symbols in the line are the same, add the winnings for that symbol and line to the total winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# function to get the slot machine spins
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    
    # Create a list of all symbols in the slot machine
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    
    # create each column in the slot machine
    for _ in range(cols):
        column = []
        
        # create a copy of all_symbols list using slicing
        current_symbols = all_symbols[:]
            
        # create a for loop that fills each row in the current column with a randomly chosen symbols
        for _ in range(rows):

            # randomly chose a symbol then remove it from current symbols so that it can e chosen again
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# function to print the slot machine columns in a grid format
def print_slot_machine(columns):

    # loop through each row of the slot machine display
    for row in range(len(columns[0])):

        # loop through each column in the row
        for i, column in enumerate(columns):

            # if statement that prints the symbol in the column apart from the last column in the row seperating it with |  
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# function to get the users deposit amount
def deposit():

    # continously prompt the user for a deposit amount
    while True:
        amount = input("What would you like to deposit? $")

        # checks if the input is a positive integer
        if amount.isdigit():
            amount = int(amount)

            # checks if deposit or amount is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# function to get the number of lines user wants to bet on
def get_number_of_lines():

    # continously prompt the user for number of lines till valid input is given
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)

            # checks if lines are between 1 and 3
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# function to get the users bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# function to spin the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    return winnings - total_bet

# main function to run the game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")     
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()