quantity=int(input("enter the food quantity:"))
food_price=float(input("enter the food price:"))
delivery_charges=float(input("enter the delivery charges:"))
sub_total=quantity*food_price
discount=sub_total/100
total_bill=sub_total+delivery_charges-discount
print(f"discount:{discount} and total_bill:{total_bill}")