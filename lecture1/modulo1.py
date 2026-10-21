def main():
    x = int(input("Write a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
# Now define is_even here and do the % part 
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()