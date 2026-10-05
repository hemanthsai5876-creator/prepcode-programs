product_1=int(input("enter the price of 1st product:"))
product_2=int(input("enter the price of 2nd product:"))
if product_1>product_2:
    print("product_1 is expensive")
elif product_1<product_2:
    print("product_1 is cheaper")
else:
    print("both products are of same price")