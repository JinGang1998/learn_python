#n为偶数
n=int(input())

def DealEvenNumber(n):

    i=0
    while(n%2==0):
        n=n/2
        i+=1
        while n!=1 and n%2==1:
            n=(3*n+1)/2
            i+=1
    print(i)

#n为奇数
def DealOddNumber(n):

    i=0
    while n!=1 and n%2==1:
        n=(3*n+1)/2
        i+=1
        while n%2==0:
            n=n/2
            i+=1
    print(i)
if(n%2==0):
    DealEvenNumber(n)
else:
    DealOddNumber(n)
