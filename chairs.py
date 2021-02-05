price = int(input('Enter the price of one chair ='))
quantity = int(input('Enter the quantity chair ='))
total_amount = price*quantity
discount = int(total_amount*10/100)
net_ammount = total_amount-discount

print('Total amount',total_amount)
print('Total discount',discount)
print('Net cost of chair',net_ammount)


