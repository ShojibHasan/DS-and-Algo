def make_abbriation_check(words):
    for i in range(len(words)):
        len_of_words = len(words[i])
        if len_of_words <=10:
            print(words[i])
        else:
            for j in range(len_of_words):
                abbriations1 = words[i][j]
                abbriations2 = words[i][j-1]
                word_count = len_of_words-2
                final_abbriation = abbriations1+str(word_count)+abbriations2
                print(final_abbriation)
                break


count = int(input())
words=[]
for i in range(count):
    word = input()    
    words.append(word)
abbriation = make_abbriation_check(words)
