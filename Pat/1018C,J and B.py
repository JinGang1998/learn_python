n = int(input())
vc1,vb1,vj1,e,vc2,vb2,vj2=0,0,0,0,0,0,0
for i in range(n):
    a = input().split()
    if a[0]=='C' and a[1]=='J':
        vc1+=1
    elif a[0]=='B' and a[1]=='C':
        vb1+=1
    elif a[0]=='J' and a[1]=='B':
        vj1+=1
    elif a[0]=='C' and a[1]=='B':
        vb2+=1
    elif a[0]=='B' and a[1]=='J':
        vj2+=1
    elif a[0]=='J' and a[1]=='C':
        vc2+=1
    else:
        e+=1
print(vc1+vb1+vj1,e,int(n)-e-vc1-vb1-vj1)
print(vc2+vb2+vj2,e,int(n)-e-vc2-vb2-vj2)
if vb1>=vc1 and vb1>=vj1:
    s='B'
elif vc1>=vj1 and vc1>vb1:
    s='C'
else:
    s='J'
if vb2>=vc2 and vb2>=vj2:
    s1='B'
elif vc2>=vj2 and vc2>vb2:
    s1='C'
else:
    s1='J'
print(s,s1)

