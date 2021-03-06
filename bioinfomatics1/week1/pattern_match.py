# Code Challenge: Solve the Pattern Matching Problem.
# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.

PATTERN = "ATA"
GENOME = "GACGATATACGACGATA"

def pattern_match(genome, pattern) -> list:
    pattern_length = len(pattern)
    genome_length = len(genome)

    result = []
    for i in range(genome_length - pattern_length):
        if genome[i:i+pattern_length] == pattern:
            result.append(str(i))
    
    return result

def pattern_match1(genome:str, pattern:str) -> list:
    import re
    result = [m.start(0) for m in re.finditer(pattern, genome)]
    return result

def main():
    result = pattern_match1(GENOME, PATTERN)
    print(*result, sep = " ")

if __name__ == "__main__":
    main()