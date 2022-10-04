#However, before concluding that we have found the DnaA box of Vibrio cholerae, the careful bioinformatician should check if there are other short regions in the Vibrio cholerae genome with multiple occurrences of "ATGATCAAG" (or "CTTGATCAT"). 
# After all, maybe these strings occur as repeats throughout the entire Vibrio cholerae genome, rather than just in the ori region. This discussion implies the following computational problem.

#Pattern Matching Problem:  Find all occurrences of a pattern in a string.
#     Input: Strings Pattern and Genome.
#     Output: All starting positions in Genome where Pattern appears as a substring.

#Code Challenge (2 points): Write a function PatternMatching that solves the Pattern Matching Problem. Then add PatternMatching to Replication.py.

#Vibrio cholerae genome

# Copy your PatternMatching function below this line.

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
   
    return positions

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions

Pattern = 'CTTGATCAT'
Genome = v_cholerae

positions = PatternMatching(Pattern, Genome)

# print the positions variable

print(positions)


#After solving the Pattern Matching Problem, we discover that "ATGATCAAG" appears 17 times in the following positions of the Vibrio cholerae genome:

#116556, 149355, 151913, 152013, 152394, 186189, 194276, 200076, 224527,
#307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368

#With the exception of the three occurrences of "ATGATCAAG" in ori at starting positions 151913, 152013, and 152394, no other instances of "ATGATCAAG" form “clumps”, i.e., appear close to each other in a small region of the genome. 
# The preceding exercise verifies that the same conclusion is reached when searching for "CTTGATCAT". We now have strong statistical evidence that "ATGATCAAG"/"CTTGATCAT" may represent the hidden message to DnaA to start replication.