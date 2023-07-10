# import socket module
from socket import *
import sys  # In order to terminate the program


# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)


# Prepare a sever socket
# Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Fill in end
while True:

    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print('Printed message is: ', message)
        filename = message.split()[1]
        print('Printed file name is: ', filename)
        f = open(filename[1:])
        outputdata = f.read()
        print('Printed outputdata is: ', outputdata)
        # Send one HTTP header line into socket
        # Fill in start
        # sends a 200 OK header line
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Fill in end
        print('length is: ', len(outputdata))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        print('File sending process is successfull (HTTP/1.1 200 OK)')

    except IOError:
        # Send response message for file not found
        # Fill in start

        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        print('File sending process is not successfull (HTTP/1.1 404 Not Found)')

        # Fill in end

    # Close client socket
    # Fill in start
        connectionSocket.close()
    # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
