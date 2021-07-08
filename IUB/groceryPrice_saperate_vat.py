apple = int(input("Enter the amount of apple in kg: "))
orange = int(input("Enter the amount of orange in kg: "))
banana = int(input("Enter the amount of banana in Dozen: "))
mango = int(input("Enter the amount of mango in kg: "))
oil = int(input("Enter the amount of Oil in Litre: "))

# apple price
apple_price = 120*apple
apple_vat_amount = apple_price*0.10
total_apple_price = apple_price+apple_vat_amount

# Orange
orange_price = 150*orange
orange_vat_amount = orange_price*0.05
total_orange_price = orange_price+orange_vat_amount

# Banana
banana_price = 60*banana
banana_vat_amount = banana_price*0.07
total_banana_price = banana_price+banana_vat_amount

# Mango
mango_price = 80*banana
mango_vat_amount = mango_price*0.02
total_mango_price = mango_price+mango_vat_amount

# Oil
oil_price = 110*oil
oil_vat_amount = oil_price*0.16
totla_oil_price = oil_price+oil_vat_amount


total_price = total_apple_price + total_orange_price+total_banana_price+total_mango_price+totla_oil_price

total_vat = apple_vat_amount+orange_vat_amount+banana_vat_amount+mango_vat_amount+totla_oil_price

final_price = total_price + total_vat

print("Price: ",final_price)

