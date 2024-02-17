import socket
import colorama
colorama.init()

def get_hostname_IP():
    hostname = input(f"\nenter URL: ")
    try:
        print(colorama.Fore.GREEN + hostname)
        print(socket.gethostbyname(hostname))
    except Exception as ex:
        print(ex)

get_hostname_IP()