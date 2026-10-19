def hello(to="World"):
    print("Hello", to)

hello()
name = input("Whats your name: ")
hello(name.title().strip())