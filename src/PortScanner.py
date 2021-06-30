
import sys
import socket

print("\nBienvenido a PortScanner-by-IIT")
print("Espero que esta herramienta pueda ser de tu ayuda")
print("La herramienta es un pelín lenta, tarda 1 min aproximadamente en realizar el scan")
print("En el futuro se mejorará la velocidad\n")

def get_host():
    try:
        objetivo  = socket.gethostbyname(input("Introduzca la dirección IP o dominio: "))
        print("Dirección IP válida!")
    #Permite salir del programa con Control+C
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("Dirección IP no encontrada")
        objetivo = get_host()
    return objetivo

objetivo = get_host()

print("En proceso de scan del objetivo: " + objetivo )

try:
    print("Escaneando los primeros 150 puertos...")
    for port in range(0,150) :
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print(f"\nEl Puerto {port} está abierto.")
        s.close() 
    print("\n")
except:
        print("\nSaliendo...")
        sys.exit(0)
