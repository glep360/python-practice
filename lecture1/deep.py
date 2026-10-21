x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? :")
# in [...] checks whether the answer matches any item in the list
if x in ["42", "forty-two", "forty two"]:
    print("Yes".strip().lower())
else:
    print("No")