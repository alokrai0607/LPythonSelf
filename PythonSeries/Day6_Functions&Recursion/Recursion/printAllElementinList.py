def printAll(list,idx):
    if(list==0):
        return 
    return printAll(list[idx])

a = [1,2,3,4,5]
print(a)