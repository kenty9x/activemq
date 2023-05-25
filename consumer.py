import stomp

class MyListener(stomp.ConnectionListener):
    def on_message(self, message):
        print("Received message:", message)

# Create a connection to ActiveMQ
conn = stomp.Connection(host_and_ports=[('localhost', 61613)])

# Set the listener to handle incoming messages
listener = MyListener()
conn.set_listener('', listener)

# Set authentication credentials
username = 'admin'
password = 'admin'

# Connect to ActiveMQ with authentication
conn.connect(username=username, password=password)

# Subscribe to a queue and start receiving messages
conn.subscribe(destination='/queue/my_queue', id=1, ack='auto')

# Wait for messages
while True:
    pass  # You can perform other tasks here or add a condition to exit the loop

# Disconnect from ActiveMQ
conn.disconnect()
