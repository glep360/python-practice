x = int(input("Write your marks (1-100): "))
if x >= 90 and x <= 100:
    print("Grade :A")
elif x >= 75 and x <= 90:
    print("Grade :B")
elif x >= 60 and x <= 75:
    print("Grade :C")
elif x >= 50 and x <= 60:
    print("Grade :D")
elif x >= 35 and x <= 50:
    print("Grade :F")
elif x >= 0 and x <= 35:
    print("Fail")
else:
    print("Error! Write correct marks")