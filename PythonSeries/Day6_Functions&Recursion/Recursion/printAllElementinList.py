def printAll(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    printAll(list,idx+1)

a = [1,2,3,4,5]
printAll(a)