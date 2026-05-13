# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
