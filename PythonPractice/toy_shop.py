
price_of_puzzle=2.60;
price_of_doll=3;
price_of_bear=4.10;
price_of_minion=8.20;
price_of_truck=2;

price_of_excursion=float(input());

number_of_puzzles=int(input());
number_of_dolls=int(input());
number_of_bears=int(input());
number_of_minions=int(input());
number_of_trucks=int(input());


total_price_of_toys=((number_of_puzzles*price_of_puzzle)+(number_of_dolls*price_of_doll)+(number_of_bears*price_of_bear)+(number_of_minions*price_of_minion)+(number_of_trucks*price_of_truck));
total_number_of_toys=number_of_puzzles+number_of_dolls+number_of_bears+number_of_minions+number_of_trucks;

if total_number_of_toys >=50:
    total_price_of_toys*=0.75;

total_price_of_toys=(total_price_of_toys*0.90);

if total_price_of_toys>=price_of_excursion:
 print(f"Yes! {(total_price_of_toys-price_of_excursion):.2f} lv left.");
else:
   print(f"Not enough money! {(price_of_excursion-total_price_of_toys):.2f} lv needed.");