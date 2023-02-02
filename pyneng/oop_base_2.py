import time
import telnetlib


class IPAddress:
    """
    Работа с IP адресами
    """

    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask

    def info(self):
        print(f'{self.ip}/{self.mask}')

    def get_bin(self):
        octets = [f"{int(octet):08b}" for octet in self.ip.split('.')]
        return '.'.join(octets)


class CiscoTelnet:
    """
    Подключение к оборудованию Cisco IOS через telnet
    """

    def __init__(self, ip: str, username: str, password: str, enable: str, disable_paging=True):
        self.ip = ip  # создан атрибут "ip"

        self._telnet = telnetlib.Telnet(ip)  # создан защищенный атрибут "_telnet"
        #  далее манипуляции с атрибутом "_telnet":
        self._telnet.read_until(b'Username:')
        self._telnet.write(username.encode('utf-8') + b'\n')
        self._telnet.read_until(b'Password:')
        self._telnet.write(password.encode('utf-8') + b'\n')
        self._telnet.write(b'enable\n')
        self._telnet.read_until(b'Password:')
        self._telnet.write(enable.encode('utf-8') + b'\n')
        if disable_paging:
            self._telnet.write(b'ter lenght 0\n')
        time.sleep(1)
        self._telnet.read_very_eager()

    def get_prompt(self):
        self._telnet.write(b'\n')
        raw_name = self._telnet.read_very_eager()
        hostname = raw_name.strip(b'\r\n#>').decode()
        print(hostname)
        return hostname

    def send_show(self, command):
        """
        Отправка show комманд
        :param command: str
        :return: str
        """
        self._telnet.write(f'{command}\n'.encode('utf-8'))
        output = self._telnet.read_until(b'#').decode('utf-8')
        return output.replace('\r\n', '\n')

    def close(self):
        self._telnet.close()

    def get_config(self):
        return self.send_show('show run')


if __name__ == '__main__':
    ip1 = IPAddress('10.10.10.1', 30)
    ip2 = IPAddress('172.17.1.9', 29)
    vars()
    vars(ip1)
    print(ip1.get_bin())
