import socket
import threading
import time
def doo():
  time.sleep(5)
  s=socket.create_connection(("0.0.0.0",6044))
  content = "Hello World!"
  # <mode>/<version>/<from>/<to>/<content_byte_size>
  
  s.send(b'G/1/@foo/@woo/'+str(len(content)).encode('ascii'))
  #follow-up/<content>
  s.send(content.encode('ascii'))

def do():
  threading.Thread(target=doo).start()