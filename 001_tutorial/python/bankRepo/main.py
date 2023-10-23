import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winning += values[symbol] * bet
                winning_lines.append(line + 1)

    return winning, winning_lines


def get_slot_machine_spin(rows: int, cols: int, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How many like to deposit? $$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How many line do yo want? (1-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be greater than between 1 and {MAX_LINES}")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet = input(f"How many bte do you want? ({MIN_BET}-{MAX_BET}) ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be greater than between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You dont have enougth money in yor ammount, yor current is {balance}"
            )
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines: {winning_lines}")
    return winnings - total_bet


def main():
    balance = deposit()

    while True:
        print(f"Current balance is: {balance}")

        spin = input("Press enter to game!! (q == quit)")

        if spin == "q":
            break
        balance += game(balance)

    print(f"YOU left in {balance}$$")


main()
