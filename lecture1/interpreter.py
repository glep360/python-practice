# .split(" ") turns "1 + 1" into three pieces. :.1f prints one digit after the decimal point
a = (input("Math expression: ").strip())
x, y, z = a.split(" ")
# x, y, z is for three exp. ike 1 + 1 
x = float(x)
z = float(z)
if y == "+":
    b = x + z
elif y == "-":
    b = x - z
elif y == "*":
    b = x * z
elif y == "/":
    b = x / z
print(f"{b:.1f}")