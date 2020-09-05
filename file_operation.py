#f=open("from_file_operation.py","w")
#f.write("print('this file is created from file_operation.py')")
with open("from_file_operation.py","r")as f:
    x=f.read()
    print(x)

with open("functions.py","r") as g:
    y=g.read()
    print(y)