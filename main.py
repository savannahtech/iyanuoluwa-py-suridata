import random
from multiprocessing import Pool, Manager, Lock, cpu_count


# The function below validates and clean the input.
# It also makes sure duplicate inputs are removed
def validate_and_clean(employee_template):
    unique_employees = []
    seen_combinations = set()

    for employee in employee_template:
        combination = (employee["name"], employee["department"], employee["age"])
        if combination not in seen_combinations:
            seen_combinations.add(combination)
            unique_employees.append(employee)

    return unique_employees


# The function below pairs the employee following the guidelines provided
def create_pairs(employee_chunk):
    employee_tuples = []
    n = len(employee_chunk)

    for i in range(n):
        employee1 = employee_chunk[i]
        employee2 = employee_chunk[(i + 1) % n]  # Wrap around to the first employee for the last one
        employee_tuples.append((employee1["name"], employee2["name"]))

    return employee_tuples


def chunk_employee(employees):
    num_employees = len(employees)
    num_available_processors = cpu_count()
    num_processes = num_available_processors
    # Adjust the number of processes based on the length of the employees list
    if num_employees < num_available_processors:
        num_processes = num_employees
    elif num_employees < 2 * num_available_processors:
        # If there are fewer employees than twice the available processors, use half of them
        num_processes = num_available_processors // 2
    # Split the data into chunks for parallel processing
    chunk_size = num_employees // num_processes
    return num_processes, chunk_size


# Function to process a chunk of employee data
def process_chunk(employee_template):
    random.shuffle(employee_template)
    pairs = create_pairs(employee_template)
    return pairs


# Main execution block with sample data
def main():
    employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        },
        {
            "department": "Sales",
            "name": "Sterling Walton",
            "age": 28
        },
        {
            "department": "R&D",
            "name": "Louis Mcintosh",
            "age": 33
        },
        {
            "department": "R&D",
            "name": "Joyce Randolph",
            "age": 29
        },
        {
            "department": "R&D",
            "name": "Oliver Mcconnell",
            "age": 63
        },
        {
            "department": "Support",
            "name": "Jimena Roman",
            "age": 22
        },
        {
            "department": "Support",
            "name": "Ellis Davenport",
            "age": 25
        },
        {
            "department": "Sales",
            "name": "Jorge Good",
            "age": 29
        },
        {
            "department": "R&D",
            "name": "Sasha Horn",
            "age": 50
        },
        {
            "department": "Sales",
            "name": "Aracely Nguyen",
            "age": 63
        },
        {
            "department": "Support",
            "name": "Kenyon York",
            "age": 71
        },
        {
            "department": "R&D",
            "name": "Oliver Mcconnell",
            "age": 63
        },
        {
            "department": "Sales",
            "name": "Saniyah Luna",
            "age": 27
        },
        {
            "department": "R&D",
            "name": "Abigayle Sosa",
            "age": 29
        },
        {
            "department": "R&D",
            "name": "Elisha Andrade",
            "age": 24
        },
        {
            "department": "Sales",
            "name": "Abril Schaefer",
            "age": 22
        },
        {
            "department": "R&D",
            "name": "Katrina Hanna",
            "age": 21
        },
        {
            "department": "R&D",
            "name": "Kaiya Fry",
            "age": 28
        },
        {
            "department": "R&D",
            "name": "Shyann Harmon",
            "age": 33
        },
        {
            "department": "R&D",
            "name": "Darnell Rangel",
            "age": 31
        },
        {
            "department": "R&D",
            "name": "Kendall Cochran",
            "age": 37
        },
        {
            "department": "R&D",
            "name": "Kylan Cantrell",
            "age": 28
        },
        {
            "department": "R&D",
            "name": "Amiah Powell",
            "age": 29
        },
        {
            "department": "R&D",
            "name": "Maria Kelley",
            "age": 22
        },
        {
            "department": "R&D",
            "name": "Jay Gonzales",
            "age": 43
        },
        {
            "department": "R&D",
            "name": "Shea Robles",
            "age": 29
        },
        {
            "department": "R&D",
            "name": "Kenyon Patel",
            "age": 23
        },
        {
            "department": "Support",
            "name": "Esmeralda Harris",
            "age": 33
        },
        {
            "department": "Sales",
            "name": "Donovan Petersen",
            "age": 23
        },
        {
            "department": "Sales",
            "name": "Ralph Yu",
            "age": 25
        },
        {
            "department": "R&D",
            "name": "Nadia Hernandez",
            "age": 26
        },
        {
            "department": "Support",
            "name": "Finley Vang",
            "age": 27
        },
        {
            "department": "R&D",
            "name": "Kelvin Cameron",
            "age": 44
        },
        {
            "department": "Support",
            "name": "Zack Barnes",
            "age": 23
        },
        {
            "department": "R&D",
            "name": "Evelyn Roth",
            "age": 23
        },
        {
            "department": "Sales",
            "name": "Charlize Cobb",
            "age": 47
        },
        {
            "department": "Sales",
            "name": "Devin Benitez",
            "age": 23
        },
        {
            "department": "R&D",
            "name": "Jaidyn Noble",
            "age": 70
        },
        {
            "department": "Sales",
            "name": "Jaydin Braun",
            "age": 63
        },
        {
            "department": "Sales",
            "name": "Anthony Bray",
            "age": 51
        },
        {
            "department": "Sales",
            "name": "Leila Becker",
            "age": 55
        },
        {
            "department": "R&D",
            "name": "Simon Walker",
            "age": 57
        },
        {
            "department": "R&D",
            "name": "Alan Kemp",
            "age": 22
        },
        {
            "department": "R&D",
            "name": "Elliot Cantu",
            "age": 23
        },
        {
            "department": "Support",
            "name": "Fiona Pearson",
            "age": 25
        },
        {
            "department": "Sales",
            "name": "Clara Bradley",
            "age": 23
        },
        {
            "department": "R&D",
            "name": "Aimee Mcpherson",
            "age": 38
        },
        {
            "department": "R&D",
            "name": "Quinn Reese",
            "age": 43
        },
        {
            "department": "Sales",
            "name": "Houston Nguyen",
            "age": 33
        },
        {
            "department": "Support",
            "name": "Jayleen Henry",
            "age": 37
        },
        {
            "department": "Sales",
            "name": "Terrance Gallagher",
            "age": 23
        },
        {
            "department": "R&D",
            "name": "Axel Bolton",
            "age": 23
        },
        {
            "department": "Sales",
            "name": "Dario Robertson",
            "age": 23
        },
        {
            "department": "Sales",
            "name": "Nadia David",
            "age": 82
        },
        {
            "department": "Support",
            "name": "Grayson Barrera",
            "age": 30
        },
        {
            "department": "Support",
            "name": "Lillie Pollard",
            "age": 30
        },
        {
            "department": "R&D",
            "name": "Desiree Carey",
            "age": 30
        },
        {
            "department": "R&D",
            "name": "Jaden Hardin",
            "age": 30
        },
        {
            "department": "Sales",
            "name": "Jason Jimenez",
            "age": 30
        },
        {
            "department": "Sales",
            "name": "Jordyn May",
            "age": 32
        },
        {
            "department": "Sales",
            "name": "Alvaro Haley",
            "age": 33
        },
        {
            "department": "Sales",
            "name": "Zackary Nguyen",
            "age": 54
        },
        {
            "department": "Support",
            "name": "Lilliana Wood",
            "age": 42
        },
        {
            "department": "Support",
            "name": "Koen Luna",
            "age": 24
        },
        {
            "department": "Sales",
            "name": "Taniyah Ramos",
            "age": 21
        },
        {
            "department": "Sales",
            "name": "Messiah Glover",
            "age": 20
        },
        {
            "department": "R&D",
            "name": "Jazmine Massey",
            "age": 29
        },
        {
            "department": "Support",
            "name": "Carolina Rowe",
            "age": 28
        },
        {
            "department": "Sales",
            "name": "Heaven Bartlett",
            "age": 26
        },
        {
            "department": "Sales",
            "name": "Harry Peterson",
            "age": 44
        },
        {
            "department": "Sales",
            "name": "Francisco Escobar",
            "age": 69
        },
        {
            "department": "Support",
            "name": "Brendon Osborne",
            "age": 65
        },
        {
            "department": "Support",
            "name": "Yuram Henson",
            "age": 55
        },
        {
            "department": "R&D",
            "name": "Lindsey Hines",
            "age": 48
        },
        {
            "department": "R&D",
            "name": "Brayden Young",
            "age": 35
        },
        {
            "department": "Support",
            "name": "Rhianna Potter",
            "age": 30
        },
        {
            "department": "Support",
            "name": "June Hanna",
            "age": 19
        },
        {
            "department": "R&D",
            "name": "Eli Buck",
            "age": 20
        },
        {
            "department": "R&D",
            "name": "Shayna Burke",
            "age": 65
        },
        {
            "department": "Support",
            "name": "Kristopher Sanders",
            "age": 62
        },
        {
            "department": "R&D",
            "name": "Tate Yates",
            "age": 52
        },
        {
            "department": "Sales",
            "name": "Hayden Massey",
            "age": 50
        },
        {
            "department": "R&D",
            "name": "Grady Baird",
            "age": 51
        },
        {
            "department": "Sales",
            "name": "Dalia Gomez",
            "age": 44
        },
        {
            "department": "Support",
            "name": "Riley Fowler",
            "age": 48
        },
        {
            "department": "R&D",
            "name": "Madilyn Melton",
            "age": 37
        },
        {
            "department": "R&D",
            "name": "Omar Browning",
            "age": 39
        },
        {
            "department": "R&D",
            "name": "Melody Nielsen",
            "age": 44
        },
        {
            "department": "R&D",
            "name": "Camron Jacobs",
            "age": 30
        },
        {
            "department": "R&D",
            "name": "Royce Moore",
            "age": 41
        },
        {
            "department": "Support",
            "name": "Ariel Reed",
            "age": 42
        },
        {
            "department": "Support",
            "name": "Yuram Henson",
            "age": 55
        },
        {
            "department": "Sales",
            "name": "Kaleb Benitez",
            "age": 51
        },
        {
            "department": "Sales",
            "name": "Mariyah Park",
            "age": 52
        },
        {
            "department": "Sales",
            "name": "Saige Castro",
            "age": 40
        },
        {
            "department": "Sales",
            "name": "Kristin Dorsey",
            "age": 61
        },
        {
            "department": "Support",
            "name": "Reed Parks",
            "age": 62
        },
        {
            "department": "R&D",
            "name": "Gerald Booker",
            "age": 43
        },
        {
            "department": "Support",
            "name": "Bennett Wolf",
            "age": 23
        },
        {
            "department": "Support",
            "name": "Abby Zuniga",
            "age": 30
        },
        {
            "department": "R&D",
            "name": "Vaughn Phelps",
            "age": 19
        },
        {
            "department": "R&D",
            "name": "Aditya Wilkerson",
            "age": 27
        },
        {
            "department": "Support",
            "name": "Jadon Tucker",
            "age": 26
        },
        {
            "department": "Sales",
            "name": "Erica Bullock",
            "age": 34
        },
        {
            "department": "Sales",
            "name": "Wilson Medina",
            "age": 36
        },
        {
            "department": "Support",
            "name": "Justice Boyle",
            "age": 37
        },
        {
            "department": "Support",
            "name": "Mina Caldwell",
            "age": 44
        }
    ]
    # Removing duplicates and validating the input
    employee_template = validate_and_clean(employees)
    num_of_process, chunk_size = chunk_employee(employee_template)
    # Splitting the data into chunks for parallel processing
    chunks = [employee_template[i:i + chunk_size] for i in range(0, len(employee_template), chunk_size)]
    # Creating a Pool of processes
    pool = Pool(num_of_process)
    # Mapping the process to the data chunks
    results = pool.map(process_chunk, chunks)
    pool.close()
    pool.join()
    final_output = [pair for sublist in results for pair in sublist]
    print(final_output)


if __name__ == "__main__":
    main()

