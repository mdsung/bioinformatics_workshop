INPUT="TCTTGATCA"

ATGC_MAP = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
}

def create_complement(gene):
    result = [ATGC_MAP[char] for char in INPUT[::-1]]
    return "".join(result)

def main():
    complement = create_complement(INPUT)
    print(complement)

if __name__ == "__main__":
    main()