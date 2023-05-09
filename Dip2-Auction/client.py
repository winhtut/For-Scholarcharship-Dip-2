import  socket
from sys import getsizeof

class Client:
    def __init__(self,client_sms):
        self.target_host ='localhost'
        self.target_port = 9991
        self.ClientMessage =bytes(client_sms,'utf-8')

        self.iden = bytes(',','utf-8')

    def runClient(self):
        client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client.connect((self.target_host,self.target_port))

        print(f'Type of sms{type(self.ClientMessage)}')
        smsAndKey = self.ClientMessage
        client.send(smsAndKey)

        recvFromServer=client.recv(4096)
        print(f'Back received from server: {recvFromServer.decode("utf-8")}')

        client.close()

if __name__=="__main__":
    while True:
        Clientsms = input("Enter data to send>:")
        print("Original Data Size is:> {0} bytes".format(getsizeof(Clientsms)))

        tcpClient = Client(Clientsms)
        tcpClient.runClient()
