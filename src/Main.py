import sys
sys.path.append('src/')
from FIFO import FIFO
from LRU import LRU
from SecondChance import SecondChance

def main():
    ref_string = "1,0;1,1;2,0;1,1;2,1;3,0;1,3;0,0"
    references = [(int(ref.split(',')[0]), int(ref.split(',')[1])) for ref in ref_string.split(';')[:-1]]

    algorithms = [FIFO(), LRU(), SecondChance()]

    for algo in algorithms:
        for ref in references:
            algo.access_page(ref[1])
        print(f"{type(algo).__name__} Page Faults: ", algo.get_page_faults())

if __name__ == "__main__":
    main()
