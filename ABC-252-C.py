N=int(input())
S = []
for i in range(N):
  s = input()
  S.append(s)

b=[0]*10
for i in range(10):
    c=[0]*10
    for j in range(N):
        a=int(S[j][i]) #標準入力した文字列を
        c[a]+=1
        b[a]=max(b[a],i+10*(c[a]-1))　#index(a)でリスト内の特定の文字を引き抜ける
print(min(b))　#わからん

#ゆっくり他の人の答えを見ながら写したが各文で何をしているかが理解できていない→A.Bを何度もやって解決できる？