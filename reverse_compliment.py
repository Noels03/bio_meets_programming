#The reverse complement of a DNA string Pattern is the string formed by taking the complementary nucleotide of each nucleotide in Pattern, then reversing the resulting string. 
# For example, the reverse complement of "AGTCGCATAGT" is "ACTATGCGACT". This leads us to the following computational problem.

#Reverse Complement Problem:  Find the reverse complement of a DNA string.
#     Input: A DNA string Pattern.
#     Output: The reverse complement of Pattern.

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern    

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    return Pattern[::-1]

rev = Reverse('')
print(rev)

# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
    basepairs = {"A":"T", "C":"G", "T":"A", "G":"C"}
    rev_pattern = ''
    for base in Pattern:
        rev_pattern += basepairs.get(base)
    return rev_pattern

