# SURIDATA  DWARF-GIANT GAME

This repository contains the solution to the Dwarf-Giant game exercise for the SURIDATA task.


## Purpose of the Project

The project is to implement a "Dwarf-Giant" game using Python. The game involves creating unique pairs of employees, ensuring each employee acts as both a dwarf and a giant exactly once.

### Key Features

1. **Input Validation:**
   - Handle duplicates in the input.
   - The unique index is a combination of the employee's name, department, and age.

2. **Random Output:**
   - The output will be random on each execution.

3. **Pair Combination:**
   - It forbid pairs such as (employee_1, employee_2) and (employee_2, employee_1).

4. **Output Format:**
   - The output is a list of tuples, where each tuple consists of the dwarf's name and the giant's name.

### Bonus Implementation

- Solution process multiple chunks with multiple threads.

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
[('Reed Parks', 'Taniyah Ramos'), ('Louis Mcintosh', 'Quinn Reese'), ('Kristin Dorsey', 'Terrance Gallagher'),
('Nadia Hernandez', 'Jayleen Henry'), ('Evelyn Roth', 'Jay Gonzales'), ('Finley Vang', 'Brayden Young'),
('Jaydin Braun', 'Gerald Booker'), ('Alvaro Haley', 'Kaleb Benitez'), ('Maria Kelley', 'Shayna Burke'),
('Grayson Barrera', 'Joyce Randolph'), ('Heaven Bartlett', 'Carolina Rowe'), ('Zack Barnes', 'Darnell Rangel'),
('Taniyah Ramos', 'Saniyah Luna'), ('Jorge Good', 'Heaven Bartlett'), ('Axel Bolton', 'Abril Schaefer'),
('Saniyah Luna', 'Jason Jimenez'), ('Madilyn Melton', 'Alan Kemp'), ('Alan Kemp', 'Oliver Mcconnell'),
('Brayden Young', 'Omar Browning'), ('Dalia Gomez', 'Eli Buck'), ('Dario Robertson', 'Madilyn Melton'),
('Jaden Hardin', 'Jaidyn Noble'), ('Joyce Randolph', 'Bennett Wolf'), ('Jaidyn Noble', 'Desiree Carey'),
('Gerald Booker', 'Jorge Good'), ('Kristopher Sanders', 'Francisco Escobar'), ('Shyann Harmon', 'Saige Castro'),
('Eli Buck', 'Elliot Cantu'), ('Jadon Tucker', 'Charlize Cobb'), ('Fiona Pearson', 'Houston Nguyen'),
('Lillie Pollard', 'Devin Benitez'), ('Nikolas Porter', 'Esmeralda Harris'), ('Yuram Henson', 'Riley Fowler'),
('Leila Becker', 'Fiona Pearson'), ('Erica Bullock', 'Reed Parks'), ('Jazmine Massey', 'Nikolas Porter'),
('Rhianna Potter', 'Erica Bullock'), ('Harry Peterson', 'Aimee Mcpherson'), ('Shayna Burke', 'Abby Zuniga'),
('Koen Luna', 'Camron Jacobs'), ('Abigayle Sosa', 'Hayden Massey'), ('Grady Baird', 'Elisha Andrade'),
('Bennett Wolf', 'Kendall Cochran'), ('Elisha Andrade', 'Maria Kelley'), ('Kenyon York', 'Lilliana Wood'),
('Nadia David', 'Messiah Glover'), ('Mina Caldwell', 'Jazmine Massey'), ('Jayleen Henry', 'Alvaro Haley'),
('Royce Moore', 'Koen Luna'), ('Saige Castro', 'Sterling Walton'), ('Sasha Horn', 'Rhianna Potter'),
('Amiah Powell', 'Kristopher Sanders'), ('Hayden Massey', 'Brendon Osborne'), ('Devin Benitez', 'Zack Barnes'),
('Anthony Bray', 'Shea Robles'), ('Kelvin Cameron', 'Lindsey Hines'), ('Charlize Cobb', 'Ellis Davenport'),
('Riley Fowler', 'Jaydin Braun'), ('Carolina Rowe', 'Jadon Tucker'), ('Elliot Cantu', 'Abigayle Sosa'),
('June Hanna', 'Grady Baird'), ('Jordyn May', 'Ralph Yu'), ('Kaleb Benitez', 'Zackary Nguyen'),
('Zackary Nguyen', 'Shyann Harmon'), ('Melody Nielsen', 'Katrina Hanna'), ('Wilson Medina', 'Kenyon York'),
('Vaughn Phelps', 'Jimena Roman'), ('Ellis Davenport', 'Dario Robertson'), ('Ralph Yu', 'Nadia Hernandez'),
('Desiree Carey', 'Kristin Dorsey'), ('Messiah Glover', 'Simon Walker'), ('Jay Gonzales', 'Axel Bolton'),
('Abby Zuniga', 'Anthony Bray'), ('Abril Schaefer', 'Melody Nielsen'), ('Kylan Cantrell', 'Mariyah Park'),
('Sterling Walton', 'Donovan Petersen'), ('Simon Walker', 'Amiah Powell'), ('Tate Yates', 'Jaden Hardin'),
('Aracely Nguyen', 'Sasha Horn'), ('Brendon Osborne', 'Harry Peterson'), ('Kaiya Fry', 'Yuram Henson'),
('Esmeralda Harris', 'Nadia David'), ('Oliver Mcconnell', 'Kelvin Cameron'), ('Mariyah Park', 'Aracely Nguyen'),
('Lilliana Wood', 'Evelyn Roth'), ('Darnell Rangel', 'Vaughn Phelps'), ('Aimee Mcpherson', 'Aditya Wilkerson'),
('Donovan Petersen', 'Lillie Pollard'), ('Francisco Escobar', 'Grayson Barrera'), ('Camron Jacobs', 'Yuram Henson'),
('Shea Robles', 'Tate Yates'), ('Lindsey Hines', 'Ariel Reed'), ('Jason Jimenez', 'Kenyon Patel'),
('Terrance Gallagher', 'Kaiya Fry'), ('Houston Nguyen', 'Jordyn May'), ('Aditya Wilkerson', 'Clara Bradley'),
('Clara Bradley', 'Finley Vang'), ('Omar Browning', 'June Hanna'), ('Quinn Reese', 'Wilson Medina'),
('Katrina Hanna', 'Louis Mcintosh'), ('Kendall Cochran', 'Royce Moore'), ('Justice Boyle', 'Dalia Gomez'),
('Kenyon Patel', 'Leila Becker'), ('Ariel Reed', 'Oliver Mcconnell'), ('Jimena Roman', 'Kylan Cantrell')]
