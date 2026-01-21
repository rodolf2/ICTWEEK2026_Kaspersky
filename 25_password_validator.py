# Enter a password to check: PogiSiMiguel143
# Password is valid and secure.

# Enter a password to check: pogisimiguel
# X Password invalid. Requirements:
# - Must contain at least one uppercase letter
# - Must contain at least one number

password = input("Enter a password to check: ")
has1upper = False
has1num = False

for s in password:
    if(s.isupper()):
        has1upper = True
    if(s.isnumeric()):
        has1upper = True

if(has1upper and has1num and len(password) >= 8):
    print("Password is valid and secure.")
else:
    print("Password invalid. Requirements:")
    if(not has1upper):
        print("- Must contain at least one uppercase letter")
    if(not has1num):
        print("- Must contain at least one number")
    if(not len(password) >= 8):
        print("- Must be at least 8")
