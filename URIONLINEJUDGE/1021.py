monetary_value = float(input())
notes_100 = monetary_value//100
print("NOTAS:")
print("%i nota(s) de R$ 100.00"%notes_100)
notes_100E = monetary_value%100
# print("%i"%notes_100E)
notes_50 =  notes_100E//50
print("%i nota(s) de R$ 50.00"%notes_50)
notes_50E = notes_100E%50
# print("%i"%notes_50E)
notes_20 = notes_50E//20
print("%i nota(s) de R$ 20.00"%notes_20)
notes_20E = notes_50E%20
notes_10 = notes_20E//10
print("%i nota(s) de R$ 10.00"%notes_10)
notes_10E = notes_20E%10
notes_5 = notes_10E//5
print("%i nota(s) de R$ 5.00"%notes_5)
notes_5E = notes_10E%5
notes_2 = notes_5E//2
print("%i nota(s) de R$ 2.00"%notes_2)

print("MOEDAS:")

notes_2E = notes_5E%2

coin_1 = notes_2E//1
print("%i moeda(s) de R$ 1.00"%coin_1)
coin_1E = notes_2E%1
coin_50 = coin_1E//0.50
print("%i moeda(s) de R$ 0.50"%coin_50)

coin_50E = coin_50%0.50
coin_25 = coin_50E//0.25
print("%i moeda(s) de R$ 0.25"%coin_25)

coin_25E = coin_50E%0.25
coin_10 = coin_25E//0.10
print("%i moeda(s) de R$ 0.10"%coin_10)

coin_10E = coin_25E%0.10
coin_5 = coin_10E//0.05
print("%i moeda(s) de R$ 0.05"%coin_5)

coin_5E = coin_10E%0.01
coin_1 = coin_5E//0.01
print("%i moeda(s) de R$ 0.01"%coin_1)