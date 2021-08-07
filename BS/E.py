n, h, l, r = input().split()
a = list(map(int,input().split()[:n]))
dp=[]
for i in range(int(n)):
    for j in range(int(h)):
        x = (j-a[i]+h)%h
        y = (j-a[i]+1+h)%h
        dp[i][j] = dp[i-1], dp[i-1][y]

        # if(l<=j and j<=r)