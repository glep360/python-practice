x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
#round used to find the nearest integer in int like float
z = round(x + y)
#by f string for format and place the value otherwise only z print and by like z:, we use that kind for make output more good we use anything like z:~ or z:/ whatever 
print(f"{z:,}")