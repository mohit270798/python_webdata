import socket
url = input('Enter:-')
word = url.split('/')
#print (data)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((word[2], 80))
cmd = 'GET'+' '+ url+' '+ 'HTTP/1.0\r\n\r\n'
code = cmd.encode()
#print(cmd)
mysock.send(code)
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    count = count+len(data)
    print(data.decode()[0:3000],end='')
print(count)
mysock.close()
