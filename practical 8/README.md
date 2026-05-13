# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

## ASSIGNMENT 8: HOTEL BOOKING SYSTEM (Java RMI)
### THEORY TO WRITE:
Java RMI (Remote Method Invocation) allows a Java object on one computer to call 
methods on a Java object running on another computer. This makes it perfect for 
building distributed applications like a Hotel Booking System.

System Components:
1. Remote Interface: Defines the methods that can be called remotely.
   Example: bookRoom(), cancelBooking()
2. Remote Object (Server): The actual class that implements these methods and 
   runs on the server machine.
3. RMI Registry: A phonebook where the server registers its object with a name.
   Clients look up this name to get the remote object's reference.
4. Client: The user program that looks up the remote object and calls methods.

Workflow:
1. Server creates the remote object and binds it to the RMI Registry with a name.
2. Client asks the Registry for the object using that name.
3. Registry gives the client a reference (stub) to the remote object.
4. Client calls methods like bookRoom(guestName, roomNumber).
5. Server executes the method, updates its internal data (like HashMap of rooms), 
   and returns true/false to the client.

Advantages of Java RMI:
- Easy to develop: Network details are hidden.
- Language compatibility: Both sides use Java.
- Security: Built-in authentication and encryption support.
- Performance: Optimized for real-time applications.

Operations in our Hotel System:
- Book Room: Client sends guest name and room number. Server checks if room is 
  free, books it, and returns confirmation.
- Cancel Booking: Client sends guest name. Server finds and removes the booking, 
  then returns confirmation.

### FILES NEEDED:
- `HotelServiceInterface.java`
- `HotelServer.java`
- `HotelClient.java`

### HOW TO RUN (Command Line):
1. Open Terminal 1. Go to the folder containing all three .java files.
2. Compile all Java files:
   ```bash
   javac *.java
   ```
3. Start the RMI Registry (if your server doesn't create it automatically):
   ```bash
   rmiregistry 1099
   ```
   Keep this running.
4. Open Terminal 2. Go to the same folder. Run the server:
   ```bash
   java HotelServer
   ```
   You will see: `Hotel Server is running...`
5. Open Terminal 3. Go to the same folder. Run the client:
   ```bash
   java HotelClient
   ```
6. The client will show a menu:
   1. Book a room
   2. Cancel booking
   3. Exit
7. Enter 1 to book a room. Type guest name and room number.
8. Enter 2 to cancel. Type guest name.
9. The server terminal will show booking/cancellation messages too.

### IMPORTANT:
- If using BlueJ IDE: Create project, create Interface class, create HotelServer 
  and HotelClient classes, compile, right-click HotelServer and run main(), then 
  right-click HotelClient and run main().
- Do not close the server terminal while client is running.
