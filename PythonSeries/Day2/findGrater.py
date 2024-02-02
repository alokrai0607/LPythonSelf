

First = int(input("Please pass your First Number Here : "))
Second = int(input("Please pass your Second Number Here : "))
Third = int(input("Please pass your Third Number Here : "))

if(First>Second and First>Third):
    print(First," is Grater Than ",Second,"and",Third)
elif(Second>First and Second>Third):
    print(Second," is Grater Than ",First,"and",Third)
elif(Third>First and Third>Second):
    print(Third," is Grater Than ",Second,"and",First)
else:
    print("All are equal")