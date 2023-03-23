import aiohttp
import asyncio
import threading
from rich import print, inspect

# lst = []
# for i in range(10000):  # есть лимит на количество открытий файла, и он < 10000
#     # Упадет с: "OSError: [Errno 24] Too many open files: 'passwords.txt'"
#     lst.append(open('passwords.txt', 'w'))
#
# print(lst, type(lst[0]))

lst = []
for j in range(10000):
    with open('passwords.txt', 'w') as f:
        lst.append(f)
        # __exit__() закроет файл в каждой итерации
print(f'{len(lst)=}')

with open('passwords.txt', 'w') as opened_file:
    opened_file.write('Some text')
    opened_file.write('\n')
    opened_file.write('New data')

balance_lock = threading.Lock()
# balance_lock.acquire()
# balance_lock.release()

with balance_lock:
    pass  # делаем обработку


async def main():
    """
    async для использования асинхронной библиотеки
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://python.org') as response:
           print(f'Status: {response.status}')
           print(f'Content type: {response.headers["content-type"]}')
           html = await response.text()
           print(f'Body: ', html[:15], '...')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
