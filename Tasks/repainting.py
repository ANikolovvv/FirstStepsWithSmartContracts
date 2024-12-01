needed_nylon = int(input());
needed_paint = int(input());
liters_of_paint=int(input());
working_hours = int(input());

nylon_price=1.50;
paint_price=14.50
diluent_price=5.00;
bags_price=0.40;

total_price_of_nylon=((needed_nylon + 2)*nylon_price);
total_price_of_paint=((needed_paint + needed_paint*0.10)*paint_price);
total_price_of_diluent=liters_of_paint*diluent_price;

total_price_of_materials=total_price_of_nylon+total_price_of_paint+total_price_of_diluent+bags_price;
sum_of_workers=(total_price_of_materials *0.30) *working_hours;

final_price=total_price_of_materials+sum_of_workers;
print(final_price)



