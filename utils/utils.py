import csv

def load_data(filepath):
    """
    Loads names from a CSV file.
    """
    names = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    names.append(row[0])
    except FileNotFoundError:
        return None
    return names
