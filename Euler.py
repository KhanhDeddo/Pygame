def binary(b):
    base2=""
    while(b>0):
        base2+=str(b%2)
        b//=2
    return base2
def change(base2):
    lis=[]
    for i in range(len(base2)-1,-1,-1):
        if base2[i]=="1":
            lis=[i]+lis 
    return lis
def compact(a,m,lst,result,n=0):
    if n in lst:
        result*=a
    if n==lst[-1]:
        return result%m
    return compact(a**2%m,m,lst,result,n+1)

def control():
    print("Tim nghich dao cua a theo modulo m. ")
    print("2. Phuong Phap Euler.")
    while True:
        select=int(input("Chon phuong phap tim kiem hoac an 0 de shutdow: "))
        if select==0:
                print("Chuong trinh da dong.")
                break
        elif select==2:       
            a=int(eval(input("a = ")))
            b=int(eval(input("b = ")))
            m=int(eval(input("m = ")))
            result=1;
            base2=binary(b)
            lst=change(base2)
            print(f" la: {compact(a,m,lst,result)}\n")
control()
