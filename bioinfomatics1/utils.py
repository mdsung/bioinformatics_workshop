from pathlib import Path

def read_genome_file(path : Path):
    with open(path, "r") as f:
        result = f.read()
    return result