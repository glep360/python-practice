# By match we dont need to write if elif else we just make cases in match and match them with input and then match give output 
name = input("Whats your name: ")
match name:
# In python we use 'or' as '|' and just write statement 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")