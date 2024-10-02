names=set()
while True:
    name=input("To quit press enter solely \n Enter new name")
    if name!="":
        names.add(name)

    elif name=="":
        print("program is ending")
        break


print("Existing Names are:")
for i in names:
    print(i)
