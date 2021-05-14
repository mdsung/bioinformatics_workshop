from pathlib import Path

from pattern_match import pattern_match1

INPUTPATH = Path(Path(__file__).parent, "data", "Vibrio_cholerae.txt")
PATTERN = "CTTGATCAT"

def read_genome_file(path : Path):
    with open(path, "r") as f:
        result = f.read()
    return result

def main():
    genome = read_genome_file(INPUTPATH)
    result = pattern_match1(genome, PATTERN)
    print(*result, sep = " ")    

if __name__ == "__main__":
    main()