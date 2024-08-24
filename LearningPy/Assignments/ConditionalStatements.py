ask = int(input("Pass your age here : "))

if(ask<18):
    print("You are Moinor")
elif(ask>=18 & ask<65):
    print("You are an adult")
elif(ask>=65):
    print("You are a Senior Citizen")
