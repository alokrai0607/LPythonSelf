marks = int(input("Please Pass your Marks Here :"))


if(marks>=90):
    print("Grade A")
elif(marks<90 and 80<=marks):
    print("Grade B")
elif(marks<80 and marks>70):
    print("Grade C")
elif(marks==70):
    print("Grade D")
else:
    print("Pramoted with poor marks")