import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus=minus.upper()
numeros="0123456789"

base=minus+mayus+numeros

longitud = 6

for _ in range(10):
    muestra = random.sample(base, longitud)
    password= "".join(muestra)
    password_encriptado=generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))