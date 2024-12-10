stage_of_championship=input();
type_of_ticket=input();
number_of_tickets=int(input());
picture_with_the_athlete="Y";

picture_price=40;
total_price=0;


stages_of_championship=[{"Quarter final":[{"Standard":55.50},{"Premium":105.20},{"VIP":118.90}]},
                        {"Semi final":[{"Standard":75.88},{"Premium":125.22},{"VIP":300.40}]},
                        {"Final":[{"Standard":110.10},{"Premium":160.66},{"VIP":400}]},];

for stage in stages_of_championship:
    for type in stage:
     
       if type == stage_of_championship:
            ticket = stage[stage_of_championship]
            
            for ticket_type in ticket:
                key=list(ticket_type.keys())[0];
                value=list(ticket_type.values())[0];
                if type_of_ticket == key:
                    total_price=value * number_of_tickets;           
if total_price > 4000:
    total_price = total_price * 0.75
elif total_price > 2500:
    if picture_with_the_athlete == "Y":
        total_price = total_price + picture_price * number_of_tickets
    total_price = total_price * 0.90
else:
    if picture_with_the_athlete == "Y":
        total_price = total_price + picture_price * number_of_tickets
print(f"{total_price:.2f}")


