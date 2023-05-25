import stomp

# Create a connection to ActiveMQ
conn = stomp.Connection(host_and_ports=[('localhost', 61613)])

# Set authentication credentials
username = 'admin'
password = 'admin'

# Connect to ActiveMQ with authentication
conn.connect(username=username, password=password)

# Send messages
message = "Hello, ActiveMQ!"
destination = "/queue/my_queue"
conn.send(body=message, destination=destination)

# Disconnect from ActiveMQ
conn.disconnect()
