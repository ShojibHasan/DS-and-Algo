birth_days = int(input())
years= birth_days//365
yearsA = birth_days%365
months = yearsA//30
monthsM = yearsA%30
days = monthsM%30
print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
