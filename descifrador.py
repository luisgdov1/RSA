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
    bytesCifrados = lector_archivoCifrado(nombre_texto)
    llavePrivada = importarLlavePrivada(nombre_texto)
    descrifrarBytes(llavePrivada, bytesCifrados, nombre_texto)

def descrifrarBytes (llave, textoCifrado, nombre):
    cifrador = PKCS1_OAEP.new (llave)
    mensaje = cifrador.decrypt(textoCifrado)
    ruta = "objetosDescifrados/descifrado" + nombre + ".txt"
    print ("Mensaje descifrado: \n" + mensaje.decode('utf-8'))
    file = open(ruta, "w")
    file.write(mensaje.decode("utf-8"))
    file.close()


def importarLlavePrivada (nombreUsuario):
    ruta = "LlavesPrivadas/llavepriv" + nombreUsuario + ".pem"
    llaveprivada = RSA.import_key(open(ruta).read())
    return llaveprivada

def lector_archivoCifrado(nombreUsuario):
    ruta = "objetosCifrados/cifrado" + nombreUsuario + ".txt"
    archivo = open (ruta, "rb")
    textoCifrado = archivo.read()
    return textoCifrado
inicio()