hey=list(map(int,input("Enter element of list   ").strip().split()))
x=int(input("Enter first element to swap with   "))-1
y=int(input("Enter second no. to swap   "))-1
def swap(hey):
    hey[x],hey[y]= hey[y],hey[x]
    return hey
print(swap(hey))
