import socket                
import time
           
server_name = 'localhost'  
server_port = 12000
bufsize = 1024

#create TCP socket for server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client_socket.connect((server_name, server_port))
print("Connection establish to server " + server_name + ": " + str(server_port))

#file to save server hosted audio file to
filename = 'received.wav'
file_for_save = open(filename, 'wb')

#time at the start of the file transfer
start_time = time.time( )

#receive first part of file
file_data = client_socket.recv(bufsize)
#continues looping until no more data is received.
while (file_data):
   file_for_save.write(file_data)
   file_data = client_socket.recv(bufsize)

#time at the end of the file transfer 
end_time = time.time( )
file_for_save.close()

print('File transfer complete – file name:  audio.wav, saved as ' + filename)
print('Time taken: ' + '{}'.format(end_time - start_time) + ' seconds')

client_socket.close()
