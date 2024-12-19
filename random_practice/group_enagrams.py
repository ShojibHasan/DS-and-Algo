from collections import defaultdict

def group_anagrams(words):
    hashmap = defaultdict(list)
    print(hashmap)
    for word in words:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)
    return list(hashmap.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def group_anagrams(words):
    hashmap = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)
    return list[hashmap.values()]