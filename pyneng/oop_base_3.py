import time
import telnetlib
from datetime import datetime
from ipaddress import IPv4Address


class IPAddress:
    """
    Работа с IP адресами
    """
    ip_type = 'IPv4'
    all_ip = []

    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask
        self.__class__.all_ip.append(ip)
        print(f'__init__() завершил работу.\nСоздан объект {self}\n')

    def info(self):
        print(f'{type(self).ip_type}: {self.ip}/{self.mask}')

    def get_bin(self):
        octets = [f"{int(octet):08b}" for octet in self.ip.split('.')]
        return '.'.join(octets)

    def __repr__(self):
        print('Сработал __repr__ :')
        return f'IPAddress("{self.ip}, {self.mask}")'

    def __str__(self):
        print('Сработал __str__ :')
        return f'{self.ip}/{self.mask}'


if __name__ == '__main__':
    print(f'{__name__=} \nSo the all module has started.\n')
    ip1 = IPAddress('10.10.10.1', 29)
    ip2 = IPAddress('10.10.10.102', 29)
    print(ip1.all_ip)
    ip2.info()
    print(ip1)  # сработает __str__()
    print(repr(ip1))  # сработает __repr__()
