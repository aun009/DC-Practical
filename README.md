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

## ASSIGNMENT 3: FUZZY SET OPERATIONS

### THEORY TO WRITE:
A Fuzzy Set is different from a normal (crisp) set. In a normal set, an element 
either belongs (1) or does not belong (0). In a fuzzy set, an element can belong 
partially, with a membership value between 0 and 1.

Example: If "tall" is a fuzzy set, a person of height 5.5 feet might have 
membership 0.4, while a person of 6 feet might have membership 0.9.

Operations on Fuzzy Sets:

1. UNION (A ∪ B):
   For each element, take the MAXIMUM of the two membership values.
   Formula: μC(x) = max[μA(x), μB(x)]
   Alternative: μC(x) = μA(x) + μB(x) - μA(x)*μB(x)

2. INTERSECTION (A ∩ B):
   For each element, take the MINIMUM of the two membership values.
   Formula: μC(x) = min[μA(x), μB(x)]
   Alternative: μC(x) = μA(x) * μB(x)

3. COMPLEMENT (~A):
   Subtract the membership value from 1.
   Formula: μ~A(x) = 1 - μA(x)

4. DIFFERENCE (A - B):
   Formula: μA-B(x) = min[μA(x), 1 - μB(x)]

Fuzzy Relations (Cartesian Product):
- If A is a fuzzy set in X and B is a fuzzy set in Y, then A × B is a fuzzy 
  relation R in X × Y.
- The membership value is calculated as: μR(x,y) = min(μA(x), μB(y))
- This creates a matrix (relational matrix).

Max-Min Composition:
- If A is a fuzzy set and R is a fuzzy relation, then B = A ∘ R.
- For each column in R, first take minimum with A values row-wise.
- Then take maximum of those minimum values column-wise.
- Formula: μB(y) = max over x [ min(μA(x), μR(x,y)) ]

### HOW TO RUN:
1. Save the Python code in a file, for example: fuzzy_sets.py
2. Run it:
   ```bash
   python fuzzy_sets.py
   ```
3. The program will print:
   - Union of sets A and B
   - Intersection of sets A and B
   - Complement of set A
   - Difference A - B
   - Cartesian product matrix R
   - Max-Min composition result B

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

## ASSIGNMENT 5: HYBRID GA-NN (Genetic Algorithm + Neural Network)

### THEORY TO WRITE:
Genetic Algorithm (GA):
- GA is inspired by nature's evolution and natural selection.
- It works with a population of possible solutions.
- Each solution is like a "chromosome" containing parameters.
- GA uses three main operations:
  a) Selection: Choose the best solutions.
  b) Crossover: Combine two good solutions to make a new one.
  c) Mutation: Randomly change some parts to explore new possibilities.
- A Fitness Function tells how good a solution is.

Neural Network (NN):
- NN is inspired by the human brain.
- It has layers of neurons connected to each other.
- It learns from data using backpropagation to reduce error.
- Good at finding patterns in complex data.

Hybrid GA-NN:
- GA is used to find the best settings (parameters) for the Neural Network.
- Instead of manually choosing number of layers, neurons, learning rate, etc.,
  the GA automatically searches for the best combination.
- GA creates many NN configurations, trains them, and keeps the best ones.
- This hybrid approach is better than using GA or NN alone.

Application: Spray Drying of Coconut Milk
- Goal: Optimize process parameters like inlet temperature, feed flow rate, 
  air flow rate, and nozzle pressure.
- Desired output: Good moisture content, particle size, and color of dried 
  coconut milk powder.
- The hybrid model predicts the quality and finds the best settings.

Steps:
1. Collect spray drying data and clean it.
2. Define the neural network structure.
3. Decide GA parameters (population size, mutation rate, crossover rate).
4. Encode NN parameters into chromosomes.
5. Define fitness function (how accurate the NN predictions are).
6. Run GA to evolve better NN configurations over many generations.
7. Stop when maximum generations reached or fitness is good enough.
8. Use the best parameters found.

### HOW TO RUN:
1. Save the Python code as: ga_nn.py
2. Make sure you have scikit-learn installed:
   ```bash
   pip install scikit-learn
   ```
3. Run it:
   ```bash
   python ga_nn.py
   ```
4. The program will show each generation's best fitness score and parameters.
5. At the end, it prints the best neural network configuration found.

## ASSIGNMENT 6: CLONAL SELECTION ALGORITHM (CSA)

### THEORY TO WRITE:
Clonal Selection Algorithm is inspired by how our immune system works.
When a virus or bacteria (antigen) enters our body, immune cells called B-cells 
produce antibodies to fight it. The B-cells that produce the best antibodies 
are cloned (multiplied) in large numbers.

Key Concepts:
1. Clonal Selection: Best candidate solutions (antibodies) are cloned 
   proportionally to their fitness. Better solutions get more clones.
2. Affinity Maturation: After cloning, the copies undergo mutation to improve 
   them further, just like B-cells refine their antibodies.
3. Population: A group of candidate solutions.
4. Fitness (Affinity): How good a solution is at solving the problem.

Steps of CSA:
1. Create an initial population of random candidate solutions.
2. Calculate fitness of each solution.
3. Select the best solutions and clone them (more fitness = more clones).
4. Apply mutation to the cloned solutions to create diversity.
5. Calculate fitness of mutated clones.
6. Select the best solutions from both original and mutated group for the 
   next generation.
7. Repeat steps 3-6 until maximum iterations reached or good solution found.
8. Return the best solution.

### HOW TO RUN:
1. Save the Python code as: csa.py
2. Run it:
   ```bash
   python csa.py
   ```
3. The program will show the best solution found in each generation.
4. Finally, it prints the overall best solution and its fitness value.

## ASSIGNMENT 7: DEAP (DISTRIBUTED EVOLUTIONARY ALGORITHMS IN PYTHON)

### THEORY TO WRITE:
DEAP stands for Distributed Evolutionary Algorithms in Python. It is a Python 
library that makes it easy to build evolutionary algorithms.

Key Features:
- Provides ready-made tools for individuals, populations, selection, mutation, 
  and crossover.
- Supports parallel evaluation (running multiple fitness checks at the same 
  time on different processors).
- Works in distributed computing environments (multiple computers).
- Very flexible: you can customize every part of the algorithm.
- Well documented and widely used.

Basic Algorithm Steps:
1. Generate an initial population of random individuals.
2. Evaluate the fitness of every individual.
3. Repeat for many generations:
   a. Select parents based on fitness (better individuals have higher chance).
   b. Apply crossover (mating) to create children.
   c. Apply mutation to introduce small random changes.
   d. Evaluate fitness of the new children.
   e. Select which individuals survive to the next generation.
4. Stop when maximum generations reached or best fitness is good enough.
5. Output the best individual found.

### HOW TO RUN:
1. Install DEAP:
   ```bash
   pip install deap
   ```
2. Save the Python code as: deap_example.py
3. Run it:
   ```bash
   python deap_example.py
   ```
4. The program will print statistics for each generation (average, min, max).
5. At the end, it shows the best individual (solution) and its fitness.

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

## ASSIGNMENT 9: MAPREDUCE WEATHER DATA (Hadoop)

### THEORY TO WRITE:
MapReduce is a programming model for processing huge amounts of data on many 
computers together. It was made by Google and is used by Hadoop.

Two Main Phases:
1. MAP Phase:
   - Reads each line of input data.
   - Extracts important information.
   - Emits (outputs) key-value pairs.
   - In our weather example: Key = Year, Value = Temperature.

2. REDUCE Phase:
   - Receives all values for the same key from all mappers.
   - Aggregates (combines) those values.
   - In our example: Calculates average temperature for each year.
   - Then finds the year with highest (hottest) and lowest (coolest) average.

Partitioning:
- The framework automatically groups all values with the same key together 
  before sending them to the reducer.

Why MapReduce?
- Scalable: Can handle petabytes of data by adding more computers.
- Fault Tolerant: If one computer fails, the work is automatically moved to 
  another computer.
- Distributed: Data and processing are spread across the cluster.

### FILES NEEDED:
- `WeatherMapper.java`
- `WeatherReducer.java`
- `WeatherDriver.java`
- `sample_weather.txt` (input data file with format: year,temperature)

### HADOOP SETUP STEPS (One Time):
1. Install Java JDK and set JAVA_HOME.
2. Install SSH and set up passwordless login:
   ```bash
   ssh-keygen -t rsa
   ```
   ```bash
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   ```
   ```bash
   chmod 640 ~/.ssh/authorized_keys
   ```
3. Download and extract Hadoop.
4. Edit these configuration files in hadoop/etc/hadoop:
   - core-site.xml: Set fs.defaultFS to `hdfs://localhost:9000`
   - mapred-site.xml: Set mapreduce.job.tracker to localhost:9870
   - hdfs-site.xml: Set dfs.replication to 1
   - hadoop-env.sh: Set JAVA_HOME path
5. Format the NameNode:
   ```bash
   hdfs namenode -format
   ```
6. Start Hadoop:
   ```bash
   start-all.sh
   ```
7. Check if running: Open browser and go to `http://localhost:9870`

### HOW TO RUN THE MAPREDUCE JOB:
1. Create input directory in HDFS:
   ```bash
   hadoop fs -mkdir -p /user/gurukul/input
   ```
2. Copy your weather data file to HDFS:
   ```bash
   hadoop fs -put sample_weather.txt /user/gurukul/input
   ```
3. Compile your Java files with Hadoop libraries:
   ```bash
   javac -cp $(hadoop classpath) -d . *.java
   ```
4. Create a JAR file:
   ```bash
   jar -cvf weather.jar -C . .
   ```
5. Run the MapReduce job:
   ```bash
   hadoop jar weather.jar WeatherDriver /user/gurukul/input /user/gurukul/output
   ```
6. View the result:
   ```bash
   hadoop fs -cat /user/gurukul/output/part-r-00000
   ```

### IMPORTANT:
- The output folder (/user/gurukul/output) must NOT exist before running.
- If it exists, delete it first: hadoop fs -rm -r /user/gurukul/output
- Input file format should be simple, like:
  ```csv
  2020,35
  2020,38
  2021,40
  2021,36
  ```

## ASSIGNMENT 10: ANT COLONY OPTIMIZATION (ACO) FOR TSP

### THEORY TO WRITE:
Ant Colony Optimization (ACO) is an algorithm inspired by how real ants find food.
When ants search for food, they move randomly and leave behind a chemical called 
pheromone. Other ants can smell this pheromone and follow the trail. If more ants 
follow a path, the pheromone becomes stronger, attracting even more ants.

How ACO Works:
1. Initialization: Place artificial ants on starting cities.
2. Movement: Each ant chooses the next city based on:
   - Pheromone level on the path (stronger = better)
   - Heuristic information (usually 1/distance, shorter = better)
   - A probability formula combining both.
3. Pheromone Update:
   - After all ants complete their tours, pheromone on each path is updated.
   - Better (shorter) tours get MORE pheromone added.
   - All pheromones also evaporate (decrease) slightly to avoid getting stuck.
4. Termination: After many iterations, the ants converge to a good (near-best) 
   solution.

Traveling Salesman Problem (TSP):
- A salesman must visit every city exactly once and return to the starting city.
- Goal: Find the shortest possible route.
- TSP is very hard because the number of possible routes grows exponentially.
- ACO is a good heuristic to find a near-optimal solution quickly.

Advantages of ACO:
- Easy to implement.
- Flexible for many types of problems.
- Can handle multiple objectives and constraints.
- Finds good solutions even when search space is huge.

Disadvantages of ACO:
- May get stuck in suboptimal solutions if parameters are wrong.
- Can be slow if there are too many ants or iterations.
- Quality depends on initial pheromone setup.

### HOW TO RUN:
1. Save the Python code as: aco_tsp.py
2. Run it:
   ```bash
   python aco_tsp.py
   ```
3. The program will show the best tour cost found in each iteration.
4. At the end, it prints:
   - Best path (order of cities visited)
   - Best (shortest) total distance
