N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(K):
    answer="No"
    if A[B[i]-1]==max(A):
        answer="Yes"
        print(answer)
        exit()
print(answer)
