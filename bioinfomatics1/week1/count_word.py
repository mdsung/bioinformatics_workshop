def count_word(string, pattern):
    string_length = len(string)
    pattern_length = len(pattern)
    count = 0

    for i in range(0,string_length-pattern_length+1):
        if string[i:i+pattern_length] == pattern:
            count += 1

    print(count)

def main():
    string = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
    pattern = "CGCG"
    count_word(string, pattern)

if __name__ == "__main__":
    main()