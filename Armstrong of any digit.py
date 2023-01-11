
def Arm():
    x = int(input("Enter any no to check is it Armstrong or not   "))
    sum,p= 0,0
    n,t=x,x
    while(t>0):    #to check power or count of no.
        t=t//10
        p=p+1
    while(x>0):    # to check armstrong or not
        z=x%10
        sum=sum+z**p
        x=x//10
    if (sum==n):
        return "It is armstrong"
    else:
        return "It is not armstrong"
print(Arm())
