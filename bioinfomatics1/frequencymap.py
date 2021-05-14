TEXT ="ACGTTGCATGTCGCATGATGCATGAGAGCT"
K = 4

def create_frequency_map(text, k):
    freqmap = {}
    maximum_value = 0

    for i in range(0, len(text) - k):
        pattern = text[i:i+k]
        if freqmap.get(pattern):
            freqmap[pattern] += 1
            if freqmap[pattern] > maximum_value:
                maximum_value = freqmap[pattern]
        elif freqmap.get(pattern) == None:
            freqmap[pattern] = 1

    return freqmap, maximum_value

def main():
    freqmap, maximum_value = create_frequency_map(TEXT, K)
    print(freqmap)
    print(maximum_value)

if __name__ == "__main__":
    main()