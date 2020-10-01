import socket   
import time               
    
server_name = 'localhost'  
server_port = 12000
bufsize = 1024

#create TCP welcoming socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind((server_name, server_port))
#server begins listening for incoming TCP requests
server_socket.listen()                     

print("Server started listening " + server_name + ": " + str(server_port))

#server waits on incoming requests and new socket is created on return.
connection_socket, addr = server_socket.accept()

#audio file to be hosted
filename = 'audioTRM.wav'
file_hosted = open(filename,'rb')

#time at the start of the file transfer
start_time = time.time( )

#read first part of file.
file_data = file_hosted.read(bufsize)
#continues looping until no more file data is left to be read.
while (file_data):
   connection_socket.send(file_data)
   file_data = file_hosted.read(bufsize)

#time at the end of the file transfer 
end_time = time.time( )  
file_hosted.close()

print('Sending complete')   
print('Time taken: ' + '{}'.format(end_time - start_time) + ' seconds')

connection_socket.close();
server_socket.close();
