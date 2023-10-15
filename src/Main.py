import sys
sys.path.append('src/')
from FIFO import FIFO
from LRU import LRU
from SecondChance import SecondChance

def main(ref_string):
    references = [(int(ref.split(',')[0]), int(ref.split(',')[1])) for ref in ref_string.split(';')[:-1]]

    algorithms = [FIFO(), LRU(), SecondChance()]

    for algo in algorithms:
        for ref in references:
            algo.access_page(ref[1])
        print(f"{type(algo).__name__} Page Faults: ", algo.get_page_faults())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name>.py <input_file>.txt")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    try:
        with open(input_filename, 'r') as file:
            ref_string = file.read().strip()
            main(ref_string)
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)
