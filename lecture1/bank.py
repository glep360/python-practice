x = input("Greeting: ").strip().lower()
# by .strip().lower() if user input in spaces and capital this handele it we need to use it in input at starting
# startswith tell us if user input that startwith then what to print
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")