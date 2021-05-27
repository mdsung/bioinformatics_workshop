# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

pattern = 'GAGG'
text = 'TTTAGAGCCTTCAGAGG'
d = 2

def calculate_hamming_distance(genome1:str, genome2:str) -> int:
    assert len(genome1) == len(genome2)
    distance = 0
    for i in range(len(genome1)):
        if genome1[i] != genome2[i]:
            distance += 1
    return distance

def main():
    results = []
    for i in range(len(text) - len(pattern) + 1):
        string = text[i : i + len(pattern)]
        distance = calculate_hamming_distance(string, pattern)
        if  distance <= d:
            results.append(i)
            print(i, end = ' ')
    print()
    print(len(results))
    
if __name__ == '__main__':
    main()