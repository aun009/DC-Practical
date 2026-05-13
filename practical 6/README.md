# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
