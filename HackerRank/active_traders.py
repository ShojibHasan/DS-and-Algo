def mostActive(customers):
    store = dict()
    res =[]
    for i in customers:
        if i in store:
            store[i] += 1
        else:
            store[i] = 1
    for i in store.items():
        if (i[1]/len(customers))*100 >=5 or (len(customers)*5)/100 >=5:
            if(i[1]/len(customers))*100 >=(len(customers)*5)/100>=5 or (i[1]/(len(customers))*100>=5):
                res.append(i[0])
    
    return sorted(res)    
    

customers = 5
a = mostActive(customers)

# print(a)