# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
