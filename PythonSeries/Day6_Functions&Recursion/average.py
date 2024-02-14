a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def avg(a,b,c):
    avg = (a+b+c)/3
    return avg
p = avg(a,b,c)
print(round(p))