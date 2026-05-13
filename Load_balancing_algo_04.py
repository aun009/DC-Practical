import random

# Server Class
class Server:
    def __init__(self, name):
        self.name = name
        self.load = 0 # number of active requests

    def handle_request(self):
        self.load += 1

    def __str__(self):
        return f"{self.name} (Load: {self.load})"

# Load Balancer Algorithms

# Round Robin
def round_robin(servers, requests):
    print("\n--- Round Robin ---")
    index = 0
    for req in requests:
        server = servers[index % len(servers)]
        server.handle_request()
        print(f"Request {req} -> {server.name}")
        index += 1

# Least Connections
def least_connections(servers, requests):
    print("\n--- Least Connections ---")
    for req in requests:
        server = min(servers, key=lambda s: s.load)
        server.handle_request()
        print(f"Request {req} -> {server.name}")

# Random Selection
def random_selection(servers, requests):
    print("\n--- Random Selection ---")
    for req in requests:
        server = random.choice(servers)
        server.handle_request()
        print(f"Request {req} -> {server.name}")

# Simulation

# Create servers
servers = [Server("Server-1"), Server("Server-2"), Server("Server-3")]

# Simulated client requests
requests = list(range(1, 11)) # 10 requests
print("Client Requests:", requests)

# Run Algorithms
round_robin(servers, requests)

# Reset loads
for s in servers:
    s.load = 0

least_connections(servers, requests)

# Reset loads
for s in servers:
    s.load = 0

random_selection(servers, requests)

# Final Server Loads
print("\n--- Final Server Loads ---")
for s in servers:
    print(s)
  
