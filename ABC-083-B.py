N,A,B=map(int,input().split())
R=sum(list(map(int,str(N))))
S=[]

for i in range(N+1):
    if sum(list(map(int,str(i))))>=A:
        if sum(list(map(int,str(i))))<=B: 
            S.append(i)
print(sum(S))