products={}
subTotal=0
for i in range(3):
    name=input(f"Enter the name of the {i+1} product: ")
    qty=int(input(f"Enter the quantity of {i+1} the item: "))
    price=float(input(f"Enter the price of {i+1} the item: "))

    lineTotal=qty*price
    subTotal+=lineTotal

    products[name]={"quantity":qty,"price":price,"line total":lineTotal}

print(f"{'Product':<12}{'Qty':>5}{'Unit':>8}{'Line Total':>14}")

for name,details in products.items():
    print(f"{name:<12}{details['quantity']:>5}{details['price']:>8.2f}{details['line total']:14.2f}")

print('-'*39)

vat=subTotal*0.19

total=subTotal+vat

print(f"{'Subtotal':<25}{subTotal:>14.2f}\n{'VAT (19%)':<25}{vat:>14.2f}\n{'Total':<25}{total:>14.2f}")
