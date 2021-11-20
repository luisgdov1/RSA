from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import  RSA

nombre_texto = ""

def inicio():
    print ("Elige una llave privada a usar")
    print ("1.- Betito 2.- Alicia 3.- Jimenita")
    opcion = int (input())

    if opcion == 1:
        nombre_texto = "Betito"
    elif opcion == 2:
        nombre_texto = "Alicia"
    elif opcion == 3:
        nombre_texto = "Jimenita"
    else:
        print ("Valor no aceptado")
        inicio()
    textoClaro = lector_archivo(nombre_texto)
    bytesClaro = bytes(textoClaro, encoding="utf8")

    #llamar a llave publica
    ruta = "LlavesPublicas/llavepub" + nombre_texto + ".pem"
    llavepublica = RSA.import_key(open(ruta).read())
    cifrador = PKCS1_OAEP.new(llavepublica)
    textoCifrado = cifrador.encrypt(bytesClaro)
    rutacifrado = "objetosCifrados/cifrado" + nombre_texto + ".txt"
    cifrado_docs = open(rutacifrado, "wb")
    cifrado_docs.write(textoCifrado)
    cifrado_docs.close()

def lector_archivo(nombreUsuario):
    ruta = "ArchivosTXT/base" + nombreUsuario + ".txt"
    file = open(ruta, "r")
    texto = file.read()
    return texto

inicio()