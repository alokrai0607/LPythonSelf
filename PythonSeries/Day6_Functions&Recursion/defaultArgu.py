
def calculate_Product(a,b):
    mul =a*b
    print(mul) 

calculate_Product(10,20)

# def calculate_Product(a=2,b):  #default param should be first.(false)
#     mul =a*b
#     print(mul) 

# calculate_Product(20)

def calculate_Product(a,b=2):  #default param should be first.(true)
    mul =a*b
    print(mul) 

calculate_Product(20)