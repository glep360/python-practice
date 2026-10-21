x = input("Write a file name: ").strip().lower()
# in this .endswith() is used to find the output in input it check end word and if match output
if x.endswith(".gif"):
    print("image/gif")
elif x.endswith((".jpg", ".jpeg")):
# 'or' works but that '|' not work this work - elif x.endswith(".jpg") or x.endswith(".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    print("text/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")