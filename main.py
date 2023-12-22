import random
from multiprocessing import Pool, Manager, Lock


# The function below validates and clean the input.
# It also makes sure duplicate inputs are removed
def validate_and_clean(employee_template):
    unique_employees = []
    seen_combinations = set()

    for employee in employee_template:
        combination = (employee["name"], employee["role"], employee["id"])
        if combination not in seen_combinations:
            seen_combinations.add(combination)
            unique_employees.append(employee)

    return unique_employees


# The function below pairs the employee following the guidlines provided
def create_pairs(employee_list, queue, paired_set, lock):
    random.shuffle(employee_list)
    pairs = set()

    for employee in employee_list:
        if not queue.empty():
          partner = queue.get()
          pair = (employee["name"], partner["name"])

        with lock:
            # This ensures the pair is not a duplicate of (employee, partner) or (partner, employee)
            # It Also, ensure an employee is not paired with themselves
            while pair in paired_set or (pair[1], pair[0]) in paired_set or pair[0] == pair[1]:
                if not queue.empty():
                  partner = queue.get()
                  pair = (employee["name"], partner["name"])
                else:
                  break

            pairs.add(pair)
            paired_set.add(pair)

    return list(pairs)


# Function to process a chunk of employee data
def process_chunk(employee_template, queue, paired_set, lock):
    cleaned_chunk = validate_and_clean(employee_template)
    pairs = create_pairs(cleaned_chunk, queue, paired_set, lock)
    queue.task_done()
    return pairs


# Main execution block with sample data
def main():
    employee_template = [
        {"name": "John", "role": "CEO", "id": 1},
        {"name": "Jane", "role": "CTO", "id": 2},
        {"name": "Bob", "role": "Manager", "id": 3},
        {"name": "Alice", "role": "Backend Dev", "id": 4},
        {"name": "Abiodun", "role": "Backend Dev", "id": 5},
        {"name": "Iyanu", "role": "Backend Dev", "id": 6},
    ]

    with Manager() as manager:
        employee_queue = manager.Queue()
        for employee in employee_template:
            employee_queue.put(employee)

        paired_set = set()
        lock = manager.Lock()

        with Pool() as pool:
            results = pool.starmap(process_chunk, [(employee_template, employee_queue, paired_set, lock)])

    final_output = [pair for sublist in results for pair in sublist]
    print(final_output)


if __name__ == "__main__":
    main()

#  Example Output:
# [('John', 'Alice'), ('Bob', 'John'), ('Abiodun', 'Jane'), ('Iyanu', 'Abiodun'), ('Alice', 'Bob'), ('Jane', 'Iyanu')]