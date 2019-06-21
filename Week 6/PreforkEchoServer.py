def preforkEchoServer():
    
    import os
    import sys
    import socket
    
    s = socket.socket()
    s.bind("localhost", 1234)
    s.listen(5)
    
    for i in range(5):
        pid = os.fork()
        if pid == 0:
            try:
                
                while True:
                    connection, address = s.accept()
                    data = connection.recv(1024)
                    
                    connection.send(data)
                    connection.close()
            
            except KeyboardInterrupt:
                sys.exit()
                
    try:
        os.waitpid(-1, 0)
    except KeyboardInterrupt:
        sys.exit()
        
preforkEchoServer()        
