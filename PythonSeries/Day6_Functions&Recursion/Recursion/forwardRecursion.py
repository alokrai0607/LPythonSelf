def fwdRec(n):
    if(n==5):
        return
    print(n)
    fwdRec(n+1)
    print("Layer Deleted in stack")

fwdRec(1)