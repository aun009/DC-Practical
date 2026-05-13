# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

## ASSIGNMENT 4: LOAD BALANCING
### THEORY TO WRITE:
Load Balancer is a component that sits between users and multiple servers. 
When many requests come from clients, the load balancer decides which server 
should handle each request. This makes sure no single server is overloaded 
while others are free.

Why is it needed?
- If one server gets all requests, it will crash.
- We want to use all servers equally for better speed and reliability.

Types shown in practical:
1. Round Robin: Requests are given to servers one by one in a cycle.
   Server 1 gets request 1, Server 2 gets request 2, Server 3 gets request 3,
   then back to Server 1 for request 4, and so on.

2. Random Selection: Each request is sent to a randomly chosen server.

Hashing Approach:
- A hash function converts the request ID into a number.
- Then we use modulo (%) with the total number of servers to pick the server.
- Example: hashed_id % server_count = destination server.

### HOW TO RUN:
1. Save the Python code as: load_balancer.py
2. Run it:
   ```bash
   python load_balancer.py
   ```
3. The program will simulate 10 client requests.
4. For each request, it will show:
   - Which server was chosen by Round Robin
   - Which server was chosen by Random selection
