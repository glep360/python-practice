def main():
    # Retrieve a valid positive number from the user
    number = get_number()
    # Call the meow function to print "Meow" that many times
    meow(number)

def get_number():
    # Loop indefinitely until a valid positive integer is provided
    while True:
        x = int(input("Write an number: "))
        if x > 0:
            # Exit the loop if the condition is met
            break
    # Return the validated positive integer
    return x

def meow(x):
    # Iterate x times based on the passed argument
    for _ in range(x):
        print("Meow\n"*2)

main()
