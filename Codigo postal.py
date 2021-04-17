import re 

cp = ""
while True:
    cp = input("Codigo postal: ")
    if bool(re.match("^\d{5}$", cp)):
        break

print("Muchas gracias!!")