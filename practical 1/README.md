# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

## ASSIGNMENT 1: RPC FACTORIAL (Python XML-RPC)
### THEORY TO WRITE:
Remote Procedure Call (RPC) is a way for one computer program to ask another 
program on a different machine to do some work, without the programmer needing 
to know network details. It works like a normal function call, but the function 
actually runs on a remote server.

Key Points:
- It uses client-server model. Client sends request, Server does the work.
- It is synchronous: the client waits until the server sends back the result.
- The client and server have different memory spaces.
- They talk to each other using messages.
- Python provides SimpleXMLRPCServer to build RPC apps easily.

Steps in RPC:
1. Client calls the remote procedure with arguments.
2. Arguments are packed into a message and sent over the network.
3. Server receives the message, unpacks arguments, and runs the procedure.
4. Server packs the result and sends it back.
5. Client receives the result and continues execution.

### FILES NEEDED:
- `factserver.py`
- `factclient.py`

### HOW TO RUN:
1. Open Command Prompt / Terminal.
2. Go to the folder where you saved the files:
   ```bash
   cd C:\Users\Student\Desktop\RPC  (Windows example)
   ```
   ```bash
   cd ~/Desktop/RPC                (Linux/Mac example)
   ```
3. First, start the server:
   ```bash
   python factserver.py
   ```
   You will see: `Factorial Server is ready to accept requests.`
4. Open a SECOND Command Prompt / Terminal window.
5. Go to the same folder again.
6. Run the client:
   ```bash
   python factclient.py
   ```
7. Enter any number when asked (or it uses 5 by default in basic code).
8. You will see output like: "Factorial of 5 is: 120"

### IMPORTANT:
- Server must be running BEFORE you run client.
- Both files should be in the same folder.
- If Python is not recognized, use "python3" instead of "python".
