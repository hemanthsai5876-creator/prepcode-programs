order_amount=int(input("order input:"))
premium_membership=input("premium membership:")
print("premium_membership")
if order_amount>=1000 or premium_membership=="yes":
    print("free delivery")
else:
    print("delivery charge applies")