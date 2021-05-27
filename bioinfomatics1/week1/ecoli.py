
from pathlib import Path
from utils import read_genome_file
from find_clump import find_clumps
INPUTFILEPATH = Path(Path(__file__).parent, "data/Ecoli.txt")

import cProfile
import functools
import pstats
import tempfile
def profile_me(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        file = tempfile.mktemp()
        profiler = cProfile.Profile()
        profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(file)
        metrics = pstats.Stats(file)
        metrics.strip_dirs().sort_stats('time').print_stats(100)
    return wraps

def find_clumps(genome, word_length, window_length, num_threshold):
    k_mer_dict = {} ## key: k-mer; value: location_list
    potential_patterns = []

    genome_length = len(genome)
    for i in range(0, genome_length - word_length):
        k_mer = genome[i : i + word_length]
        if k_mer_dict.get(k_mer): 
            k_mer_dict[k_mer].append(i)
            if len(k_mer_dict.get(k_mer)) > num_threshold:
                potential_patterns.append(k_mer)                    
        elif k_mer_dict.get(k_mer) == None:
            k_mer_dict[k_mer] = [i]

    for pattern in potential_patterns:
        k_mer_dict[pattern]

    return potential_patterns

@profile_me   
def main():
    genome = read_genome_file(INPUTFILEPATH)
    result = find_clumps(genome, 9, 500 ,3)
    print(len(result))

if __name__ == "__main__":
    main()