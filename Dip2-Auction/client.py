import socket


class TCPclient():
    def __init__(self, sms):
        self.target_ip = 'localhost'
        self.target_port = 9998
        self.send_and_recv_data = {}

        self.client_sms = bytes(sms, 'utf-8')

        self.send_and_recv_data.update({len(self.send_and_recv_data): sms})

    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        client.send(self.client_sms)

        received_from_server = client.recv(4096)

        recv_sms = received_from_server.decode("utf-8")

        self.send_and_recv_data.update({len(self.send_and_recv_data):recv_sms})
        print("Get Back Data from Server:",recv_sms)

        client.close()


if __name__ == "__main__":
    while True:
        sms = input("Enter some data to send:")
        tcp_client = TCPclient(sms)
        tcp_client.run_client()
