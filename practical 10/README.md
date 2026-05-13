# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
