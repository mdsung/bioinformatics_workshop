def imediate_neighbors(pattern):
    neighborhood = set()
    for i, symbol in enumerate(pattern):
        for x in 'ATCG':
            if x != symbol:
                neighbor = f"{pattern[:i]}{x}{pattern[i+1:]}"
                neighborhood.add(neighbor)
    return neighborhood

def main():
    print(imediate_neighbors("GCAT"))

if __name__ == '__main__':
    main()