import rpyc

# Connect to server
conn = rpyc.connect("localhost", 18861)

# Input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Call remote method
result = conn.root.concatenate(str1, str2)

# Output
print("Concatenated String:", result)
