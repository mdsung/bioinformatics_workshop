# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.

# Input: A string Text as well as integers k and d.
# Output: All most frequent k-mers with up to d mismatches in Text.

def find_neighbors(pattern, d):
    

def frequent_word_with_mismatches(text, k, d):
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(n-k):
        pattern = text[i : i+k]
        neighborhood = find_neighbors(pattern, d)
        for neighbor in neighborhood:
            if freq_map.get(neighbor) == None:
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1

    max_count = max(freq_map.valuese())
    
    for key, value in freq_map.items():
        if value == max_count:
            patterns.append(key)

def main():
    pass

if __name__ == '__main__':
    main()