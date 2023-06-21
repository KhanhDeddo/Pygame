#TIM NGICH DAO BANG EULER.
def gcd(a,m):
    if m==0:
        return a
    return gcd(m,a%m)

def primeFactorization(m):
    lis=[]
    for i in range(2,m+1):
        count=0
        while m%i==0:
            count+=1
            m//=i
        if count:
            lis.append(i)
    return lis


def inverseOfA(a,m,lis):
    s=m
    for i in lis:#Tinh phi(m).
        s=s*(1-(1/i))
    return f"{a}^{int(s-1)}"


def binary(b):
    lis=list(map(int,b.split("^")))#Tach lay so mu.
    base2=""
    while((lis[1])>0):
        base2+=str(lis[1]%2)
        lis[1]//=2
    return base2


def change(base2):
    lis=[]
    for i in range(len(base2)-1,-1,-1):
        if base2[i]=="1":
            lis=[i]+lis # chèn số mu cua 2 vào đầu danh sách.
    return lis


def compact(a,m,lst,result,n=0):
    if n in lst:
        result*=a
    if n==lst[-1]:
        return result%m
    return compact(a**2%m,m,lst,result,n+1)

def control():
    print("Tim nghich dao cua a theo modulo m. ")
    print("1. Phuong Phap Euclid mo rong.")
    print("2. Phuong Phap Euler.")
    while True:
        select=int(input("Chon phuong phap tim kiem hoac an 0 de shutdow: "))
        if select==0:
                print("Chuong trinh da dong.")
                break
        if select==1:
            a=int(eval(input("a = ")))
            m=int(eval(input("m = ")))
            inverse(a,m)
        elif select==2:       
            a=int(eval(input("a = ")))
            m=int(eval(input("m = ")))
            if gcd(a,m)==1:
                result=1 
                lis=primeFactorization(m)
                b=inverseOfA(a,m,lis)
                base2=binary(b)
                lst=change(base2)
                print(f"Nghich dao cua {a} theo modulo {m} la: {compact(a,m,lst,result)}\n")
            else:
                print(f"{a} khong co kha nghich theo modulo {m}. Vi UCLN({a},{m}) = {gcd(a,m)} != 1\n")
            
control()
