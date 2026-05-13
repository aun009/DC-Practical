# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

## ASSIGNMENT 2: RMI STRING CONCATENATION (Python Pyro4)
### THEORY TO WRITE:
Remote Method Invocation (RMI) allows an object running in one Java Virtual 
Machine (JVM) to call methods on an object running in another JVM. In Python, 
we use a library called Pyro4 (Python Remote Objects) to do the same thing.

Key Points:
- RMI lets objects talk to each other across different machines.
- Client side uses a Stub (proxy object) that looks like the real object.
- Server side uses a Skeleton that receives calls and runs the real method.
- They communicate over the Internet.
- Pyro4 makes this very easy in Python using decorators like @Pyro4.expose.

Steps in RMI:
1. Define a remote interface (class with methods to be called remotely).
2. Server creates an object, registers it with a Name Server, and waits.
3. Client looks up the object using its name.
4. Client calls methods as if the object is local.
5. Server executes the method and returns the result.

### FILES NEEDED:
- `server.py`
- `client.py`

### HOW TO RUN:
1. Install Pyro4 library first:
   ```bash
   pip install Pyro4
   ```
2. Open Terminal 1 and start the Pyro4 Name Server:
   ```bash
   pyro4-ns
   ```
   (or try: python -m Pyro4.naming)
   Keep this window running.
3. Open Terminal 2, go to your code folder, run the server:
   ```bash
   python server.py
   ```
   You will see a Server URI printed. The server also saves this to server_uri.txt.
   Keep this window running.
4. Open Terminal 3, go to the same folder, run the client:
   ```bash
   python client.py
   ```
5. Enter first string and second string when asked.
6. You will see the concatenated result.

### IMPORTANT:
- The file server_uri.txt is created automatically. Do not delete it.
- Client reads the URI from this file to connect to the server.
- All three terminals (Name Server, Server, Client) must be running together.
