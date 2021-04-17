import re
tel = ""

while not bool(re.match("^\d{3}-\d{3}-\d{4}$", tel)):
    tel = input("Ingrese el telefono en formato ###-###-####: ")

print("Muchas gracias")