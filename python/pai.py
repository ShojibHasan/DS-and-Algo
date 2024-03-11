import decimal

decimal.getcontext().prec = 1000

division = decimal.Decimal(22) / decimal.Decimal(7)
print(division)

