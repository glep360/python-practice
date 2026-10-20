#strings work fo remove something in output and make output better
name = input("Enter your name: ")
#strip() method removes any leading and trailing whitespace from the string
#title() method capitalizes the first letter of each word in the string
name = name.strip().title()
print(f"Hello, {name}!")