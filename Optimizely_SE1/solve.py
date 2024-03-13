def shirts_distribute(shirt, bags):
    if bags > shirt:
        return "Bags are more than T-Shirts"
    else:
        shirts_per_bag = shirt // bags
        extra_shirts = shirt % bags

        distribution = [shirts_per_bag] * bags

        for i in range(extra_shirts):
            distribution[i] += 1

        return distribution


shirt = int(input("Enter T-Shirt Number: "))
bags = int(input("Enter bags Number: "))

print(shirts_distribute(shirt, bags))