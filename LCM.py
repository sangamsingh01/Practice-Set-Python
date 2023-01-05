def cal_lcm(x,y):
    if x>y:
        gr=x
    else:
        gr=y
    while(1):

        if (gr%x==0)and(gr%y==0):

            lcm=gr
            return lcm
        gr+=1


n1=int(input("Enter 1st no."))
n2=int(input("Enter 2nd no."))


print("LCM is =", cal_lcm(n1,n2))
