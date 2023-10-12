def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    total = 0
    for i in range(0,len(candles)):
        if candles[0] == candles[i]:
            total+=1
    print(total)
    
    
candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)