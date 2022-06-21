import socket
import threading
import usr
def client(sock):
  # "send" mode
  f=sock.recv(100)
  f=f.decode() # so we can use .split()
  try:
    a=f.split(" ")
  except:
    sock.send(b'okay 4')
    sock.close()
    return
  if a[0] == "send":
    pass
  else: # AMOGUS SUSSY, CLOSE SOCKEY
    sock.close()
    return
  if usr.check(a[1]):
    sock.send(b'okay 1')
  else:
    sock.send(b'okay 2')
    sock.close()
    return
  oaae=a[1]
  # mode2, "what <size>"
  f=sock.recv(100)
  print(f)
  f=f.decode()
  try:
    a=f.split("what ",1)[1]
    a=int(a)
  except:
    sock.send(b'okay 4')
    sock.close()
    return
  sock.send(b'okay 1')
  # mode3, recieve lmao
  f=sock.recv(a)
  f=f.decode()
  usr.record(oaae,f)
  sock.close()
  
s=socket.create_server(("0.0.0.0",4076))
while True:
  a,b=s.accept()
  threading.Thread(target=client,args=(a,)).start()