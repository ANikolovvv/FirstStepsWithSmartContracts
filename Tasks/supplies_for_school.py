number_of_pens =int(input());
number_of_markers=int(input());
liters_of_ink=int(input());
persentage_of_price=int(input());

package_of_pens=5.80;
package_of_markers=7.20;
liter_of_ink=1.20;

total_price_of_pens=number_of_pens*package_of_pens;
total_price_of_markers=number_of_markers*package_of_markers;
total_price_of_ink=liters_of_ink*liter_of_ink;

total_price=total_price_of_pens+total_price_of_markers+total_price_of_ink;
discount=total_price*persentage_of_price/100;
final_price=total_price-discount;

rounded_number = round(final_price, 2)

print(rounded_number);
