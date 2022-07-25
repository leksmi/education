from http import client

if '__name__' == '__main__':
    conn = client.HTTPConnection('www.google.com')
    conn.request('GET', '/')
    res = conn.getresponse()
    a = 0
