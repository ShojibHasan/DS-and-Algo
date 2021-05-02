import decimal

decimal.getcontext().prec = 100

division = decimal.Decimal(22) / decimal.Decimal(7)
print(division)

