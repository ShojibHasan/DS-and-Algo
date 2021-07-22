n = int(input())

if n<3:
    print("Infancy")

elif n>3 and n<12:
    print("Childhood")
elif n>12 and n<20:
    print("Adolescence")
elif n>=20 and n<40:
    print("Young adulthood")
elif n>40 and n<65:
    print("Mature adulthood")
elif n>65:
    print("Late adulthood")