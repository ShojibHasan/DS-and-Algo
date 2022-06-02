rollNumbers=[122,233,353,456]
names =['alex','bob','can','don']

NewDictionary={i:j for (i,j) in zip (rollNumbers,names)}
print(NewDictionary.keys())
print(NewDictionary.values())
print(NewDictionary.items())

