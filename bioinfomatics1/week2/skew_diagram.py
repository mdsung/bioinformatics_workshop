# Exercise Break: Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14.

GENOME = "GAGCCACCGCGATA"

skew_idx = 0 
skew_indices =  [skew_idx]

for ch in GENOME:
    if ch == 'C':
        skew_idx = skew_idx - 1
    if ch == 'G':
        skew_idx = skew_idx + 1
    skew_indices.append(skew_idx)

print(" ".join([str(ch) for ch in skew_indices]))    

  