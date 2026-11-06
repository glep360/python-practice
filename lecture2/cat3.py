# We use while statement here also with True so if only it is true it work also use break statement for answer 
while True:
    n = int(input("Write a number: "))
    if n > 0:
        break
for _ in range(n):
    print("Meow\n" * 2)