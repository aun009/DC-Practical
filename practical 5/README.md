# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
