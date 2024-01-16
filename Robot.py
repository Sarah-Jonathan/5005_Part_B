import socket
import ssl
def create_client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        # Connect to the server using SSL/TLS
        with socket.create_connection(('localhost', 12345)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                health_data = "Temperature: 37.2, Heartbeat: 80"

                # Send health data to the server
                ssock.sendall(health_data.encode('utf-8'))
                print("Data sent to server:", health_data)

    except ConnectionRefusedError:
        print("Error: Connection to the server failed. Make sure the server is running.")

create_client()
