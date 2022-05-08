def char_is_hiragana(c) -> bool:
    return u'\u3040' <= c <= u'\u309F'
def string_is_hiragana(s: str) -> bool:
    return all(char_is_hiragana(c) for c in s)

demo_text = input()

print(demo_text, string_is_hiragana(demo_text))


# print('ひらがな', string_is_hiragana('ひらがな'))
# print('a', string_is_hiragana('a'))
# print('english', string_is_hiragana('english'))

# アアアアアなたか


# ([ぁ-ん])

special_characters = 1
s=input()
# Example: $tackoverflow

if any(c in special_characters for c in s):
    print("yes")
else:
    print("no")

