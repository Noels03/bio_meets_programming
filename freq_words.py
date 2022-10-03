#We now have a rigorously defined computational problem for finding frequent words in the replication origin. We define a computational problem as a specification of input data in addition to a precise specification of output data that will solve the problem.

#Frequent Words Problem:  Find the most frequent k-mers in a string.
#     Input: A string Text and an integer k.
#     Output: All most frequent k-mers in Text.

# Copy your updated FrequentWords function (along with all required subroutines) below this line
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] += 1
    return freq

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'

k = 10


# Finally, print the result of calling FrequentWords on Text and k.

print(FrequentWords(Text, k))