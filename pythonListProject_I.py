myListofcontacts = []

name1 = input("contact name: ")
name2 = input("contact name: ")
name3 = input("contact name: ")

myListofcontacts.append(name1)
myListofcontacts.append(name2)
myListofcontacts.append(name3)

if(myListofcontacts):
    print(myListofcontacts)

else:
    print("Empty List")