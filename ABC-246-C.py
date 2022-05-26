N,K,X=map(int,input().split())
a=list(map(int,input().split())
       
for i in range(K):
     b=min(a[i]//X,K)
     k-=b
     a[i]-=b*X
     ans=sum(a[i])
print(ans)
