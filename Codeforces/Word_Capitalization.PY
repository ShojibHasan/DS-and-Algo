s = input()

lst = [word[0].upper() + word[1:] for word in s.split()]
s = " ".join(lst)
print(s)