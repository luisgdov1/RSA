from Crypto.PublicKey import RSA
import pem

valores_e = [17, 4133, 5693]
nombres = ["Betito", "Alicia", "Jimenita"]
i=0

for valor_e in valores_e:
    llave_privada = RSA.generate(2048, None, valor_e)

    #llave publica
    llave_publica = llave_privada.publickey()

    nombre = "llavep" + nombres[i] + ".txt"

    #Llave publica a txt
    linea_inicial = "e: " + str(llave_publica.e) +"\n n: " + str(llave_publica.n) + "\n"
    texto_final = linea_inicial + str(llave_publica.exportKey())
    file = open (nombre, "w")
    file.write(texto_final)
    file.close()


    nombrepem1 = "llavepub" + nombres[i] + ".pem"
    #cifrado de llave
    f = open (nombrepem1, "wb")
    f.write(llave_publica.exportKey("PEM"))
    f.close()

    nombrepem2 = "llavepriv" + nombres[i] + ".pem"

    f = open (nombrepem2, "wb")
    f.write(llave_privada.exportKey("PEM"))
    f.close()

    i=i+1
