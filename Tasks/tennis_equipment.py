import math;

price_of_tennis_racket=float(input());
number_of_tennis_rackets=int(input());
number_of_sneakers=int(input());

sneakers_price=price_of_tennis_racket/6;
total_equipment_price=(price_of_tennis_racket*number_of_tennis_rackets)+(sneakers_price*number_of_sneakers);

other_equipment_price=total_equipment_price*0.2;
total_price_of_equipment=total_equipment_price+other_equipment_price;

players_share=total_price_of_equipment/8;
sponsors_share=total_price_of_equipment-players_share;

print(f"Price to be paid by Djokovic {math.floor(players_share)}");
print(f"Price to be paid by sponsors {math.ceil(sponsors_share)}");

