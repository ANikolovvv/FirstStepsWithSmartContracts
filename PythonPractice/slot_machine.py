import random

def spin_slot_machine():
   symbols=["7", "8", "9", "10", "J", "Q", "K", "A"];
   row=[random.choice(symbols) for _ in range(3)];
   return row;

def print_row(row):
   print(f"[{row[0]}] [{row[1]}] [{row[2]}]")

def get_payout(row,bet):
   if row[0]==row[1]==row[2]:
      return bet*10;
   elif row[0]==row[1] or row[1]==row[2] or row[0]==row[2]:
      return bet*5;
   else:
      return 0;

def main():
    balance=100;
    print("****************************")
    print("Welcome to the slot machine!")
    print("Symbols: 7, 8, 9, 10, J, Q, K, A")
    print("****************************")

    while balance>0:
        print(f"How much would you like to bet? Current balance: ${balance}")
        bet = input("Enter amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet>balance:
            print("Insufficient funds. Please enter a smaller amount.")
            continue

        if bet<=0:
            print("Please enter a positive number.")
            continue

        balance=balance-bet;
        row=spin_slot_machine();
        print("Spinning...");
        print_row(row);
        payout=get_payout(row,bet);
        if payout> 0:
            print(f"You won ${payout}!");
        else:
            print("Better luck next time!");
        balance+=payout;

        play_again=input("Do you want to play again? (y/n): ")
        if play_again != "y":
            break;
    print("*********************************")
    print(f"Thanks for playing! Your final balance is ${balance}")
    print("*********************************")

if __name__ == "__main__":
    main()

