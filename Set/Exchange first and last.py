hey=list(map(int,input("Enter element of list ").strip().split()))
def change(hey):
    hey[0],hey[-1]=hey[-1],hey[0]
    return hey
print(change(hey))
