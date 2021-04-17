import re
rfc = ""

while not bool(re.match("^[A-Z]{3,4}\d{6}[A-Z0-9]{3}$", str.upper(rfc))):
    rfc = input("Registro Federal de Contribuyentes: ")

print("Muchas Gracias!!")