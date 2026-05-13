# COMPUTER LABORATORY III (DC PRACTICALS)
## HOW TO RUN + THEORY TO WRITE IN JOURNAL
**For: BE AI&DS - Semester VIII**

### NOTE FOR STUDENTS:
- Write the theory in your own handwriting in the journal.
- Run commands exactly as shown.
- If any command fails, check that you are in the correct folder.

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
