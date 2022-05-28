H,W=map(int,input().split())
S=(input() for i in range(W) for i range(H))

for i in range(H):
    S[i]=list(S[i])
    for j in range(W):
        if S[i][j]=="o":
            start=(i,j)
            
