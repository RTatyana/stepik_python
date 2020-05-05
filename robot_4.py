t=int(input())
for ii in range(t):
    n=int(input())
    a=list(input())
    p=[[0,0,0]]
    x=0
    y=0
    for i in range(n):
        if a[i]=='L':
            x-=1
        elif a[i]=='R':
            x+=1
        elif a[i]=='U':
            y+=1
        else:
            y-=1
        p.append([x,y,i+1])
    p.sort()
    m=n+1
    for i in range(n):
        if p[i][0]==p[i+1][0] and p[i][1]==p[i+1][1]:
            if p[i+1][2]-p[i][2]<m:
                ans=[p[i][2]+1,p[i+1][2]]
                m=p[i+1][2]-p[i][2]
    #print(p)
    if m==n+1:
        print(-1)
    else:
        print(*ans)