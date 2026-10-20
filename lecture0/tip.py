def main():
    x = dollars_to_float(input("How much themeal cost :"))
    y = percent_to_float(input("what percentage to tip :"))
    z = x * y
    #x = dollar and y = percentage and the z is tip
    print(f"leave ${z:.2f}")

def dollars_to_float(d):
        #Strip the leading '$' and convert to float
        return float(d.lstrip("$"))
def percent_to_float(p):
        #strip the leading '%' and convert to float
        return float(p.lstrip("%")) /100
if __name__ == "__main__":
       main()