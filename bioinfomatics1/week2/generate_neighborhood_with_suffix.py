def calculate_hamming_distance(string1, string2):
    assert len(string1) == len(string2)
    return sum([s1 != s2 for s1, s2 in zip(string1, string2)])
        
def generate_neighbors(pattern, d):
    if d == 0:
        return {pattern}
    
    if len(pattern) == 1:
        return {"A", "T", "C", "G"}
    
    neighborhood = set()
    suffix_pattern = pattern[1:]
    suffix_neighbors = generate_neighbors(suffix_pattern, d)

    for string in suffix_neighbors:
        if calculate_hamming_distance(suffix_pattern, string) < d:
            for x in 'ATGC':
                neighborhood.add(f"{x}{string}")
        else :
            neighborhood.add(f"{pattern[0]}{string}")
    
    return neighborhood

def main():
    print(" ".join(generate_neighbors("CAGGACGT", 2)))

if __name__ == '__main__':
    main()