import time
import telnetlib
from getpass import getpass


class BaseTelnet:
    def __init__(self, ip: str,
                 username: str,
                 password: str,
                 prompt: str,
                 short_sleep: int = 1,
                 long_sleep: int = 5
                 ):
        print('__init__ base class')
        self.ip = ip
        self.username = username
        self.password = password
        self.prompt = prompt
        self.short_sleep = short_sleep
        self.long_sleep = long_sleep

        self._telnet = telnetlib.Telnet(ip, timeout=7)
        self._telnet.read_until(b'Username:')
        self._telnet.write(username.encode('utf-8') + b'\n')
        self._telnet.read_until(b'Password:')
        self._telnet.write(password.encode('utf-8') + b'\n')
        time.sleep(self.short_sleep)
        self._telnet.read_very_eager()

    def send_command(self, command: str):
        self._telnet.write(command.encode('utf-8') + b'\n')
        # time.sleep(self.long_sleep)
        # output = self._telnet.read_very_eager().decode('utf-8')
        output = self._read_until_prompt()
        return output.replace('\r\n', '\n')

    def _read_until_prompt(self):
        output = self._telnet.read_until(self.prompt.encode('utf-8'))
        return output.decode('utf-8')

    def close(self):
        '''
        Close telnet connection.
        :return: none
        '''
        self._telnet.close()


if __name__ == '__main__':
    with BaseTelnet(ip='10.252.135.34', username='nngs-sps', password=input('Password: '), prompt='>') as conn:
        print(conn.send_command('sho clock'))
