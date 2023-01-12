a=int(input("Enter the size of an array  "))

n=list(map(int, input("Enter the element of array  ").strip().split()))

z= "Something went wrong :( "

for i in range(1, a-1):
    if (n[i]==n[i+1]) :
        z="It is monotonic"
        break
    else:
        z="It is not monotonic"

print(z)
