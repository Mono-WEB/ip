import socket

def get_ip():
    hostname = input('Введіть адресу сайта ')
    try:
        return f"Адреса сайта {hostname}\nIp: {socket.gethostbyname(hostname)}"
    except socket.gaierror() as error:
        return "Не вірна адреса сайта"

def main():
    print(get_ip())

if __name__ == "__main__":
    main()