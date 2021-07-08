apple = int(input("Enter the amount of apple in kg: "))
orange = int(input("Enter the amount of orange in kg: "))
banana = int(input("Enter the amount of banana in Dozen: "))
mango = int(input("Enter the amount of mango in kg: "))
oil = int(input("Enter the amount of Oil in Litre: "))

total_price_without_vat = (120*apple)+(150*orange)+(60*banana)+(80*mango)+(110*oil)

vat = total_price_without_vat*0.15
total_price_with_vat = total_price_without_vat + vat

print("Total Price without VAT ",format(total_price_without_vat,".1f"))

print("Total Price including VAT ",format(total_price_with_vat,".1f"))