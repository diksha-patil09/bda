data = list(map(int,input("Enter Data : ").split(" ")))

def hash(x):
    return (6*x + 1) % 5
    
maxCount = 0
for i in data:
    print("Element : ",i,end="")
    x = hash(i)
    print(", Hash Value : ",x,end="")
    x = bin(x)[2:]
    print(", Binary Equivalent : ",x,end="")
    trailingZeros = 0
    i = len(x) - 1
    while i >= 0:
        if x[i] == "0":
            trailingZeros += 1
        i -= 1
    if trailingZeros == len(x):
        print(", Trailing Zeros : 0")
    else:
        maxCount = max(maxCount,trailingZeros)
        print(", Trailing Zeros : ",trailingZeros)
    
print("r : ",maxCount)
print("No of Distinct Elements : ",2**maxCount)

