
f=open("febs.py","w")
f.write("print('hello')")
f.close()


with open("if_sample.py","r") as f:
    x=f.read()

    print(x)