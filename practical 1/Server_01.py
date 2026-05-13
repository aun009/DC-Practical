from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    # Function to calculate factorial
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register function
server.register_function(factorial, "factorial")

# Run server
server.serve_forever()
