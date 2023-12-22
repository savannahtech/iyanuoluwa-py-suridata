# SURIDATA  DWARF-GIANT GAME

This repository contains the solution to the Dwarf-Giant game exercise for the SURIDATA task.


## Exercise Overview

The task is to implement a "Dwarf-Giant" game using Python. The game involves creating unique pairs of employees, ensuring each employee acts as both a dwarf and a giant exactly once.

### Exercise Guidelines

1. **Input Validation:**
   - Handle duplicates in the input.
   - The unique index is a combination of the employee's name, role, and ID.

2. **Random Output:**
   - The output should be random on each execution.

3. **Pair Combination:**
   - Forbid pairs such as (employee_1, employee_2) and (employee_2, employee_1).

4. **Output Format:**
   - The output must be a list of tuples, where each tuple consists of the dwarf's name and the giant's name.

### Bonus Task

Implement a solution that processes the input in multiple chunks using multiple processes.

## Code Overview

The Python script provided in this repository demonstrates the implementation of the Dwarf-Giant game.

### Code Components

- **Validation and Cleaning:**
  - Ensures uniqueness based on the combination of name, role, and ID.

- **Pair Generation:**
  - Randomly creates pairs following the specified guidelines.

- **Multiprocessing:**
  - Utilizes multiple processes for efficient execution.

### How to Run

1. Clone the repository using: `git clone https://github.com/savannahtech/iyanuoluwa-py-suridata.git`
2. Ensure you have Python 3.11 installed.
3. Run the script using: `python main.py`

## Sample Output

The script generates output in the form of a list of dwarf-giant pairs. Example:

```python
[('John', 'Alice'), ('Bob', 'John'), ('Abiodun', 'Jane'), ('Iyanu', 'Abiodun'), ('Alice', 'Bob'), ('Jane', 'Iyanu')]