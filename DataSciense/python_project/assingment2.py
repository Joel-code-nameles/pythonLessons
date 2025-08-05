password = input("Password: ")
if len(password) < 8:
    print("Weak")

if len(password) >= 8:
    print("Strong")

if "#" or "@" in password:
    print("Extra Strong")

if 1234567890 or password.upper() not in password:
    print("Extra Weak")