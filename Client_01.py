import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
num = int(input("Enter a number: "))

# call remote function
result = client.factorial(num)

# Display result
print("Factorial:", result)
