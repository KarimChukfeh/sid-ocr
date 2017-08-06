f = open('text.txt', 'r')
sid = f.read(7)
try:
    int(sid)
    print('yas')
    print(sid[0])
except:
    print('boo')


