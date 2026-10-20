# In scope we need to declare variable and it only lives inside that function   
def main():
    name = input("What is ypur name: ")
    hello(name.title())
def hello(to = "world"):
    print("hello", to.strip())
main()