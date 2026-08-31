# ==========================================
# 1. BASIC LOOPS (Mathematical Logic)
# ==========================================

# To print even numbers between 0 and 100:
# range(51) counts from 0 to 50 (inclusive) and multiplies each by 2.
for number in range(51):
    print(2 * number)

# To print odd numbers between 0 and 100 with a step of 2:
# Starts at 1, goes up to 100, and adds 2 at each step (1, 3, 5...).
for i in range(1, 100, 2):
    print(i)


# ==========================================
# 2. PATTERNCOUNT (Motif / Substring Counting)
# ==========================================

# The core function that counts how many times a target sequence (Pattern) 
# appears within a long DNA text (Text).
def PatternCount(Text, Pattern):
    count = 0
    # Scans the text from beginning to end using a sliding window approach.
    # len(Text) - len(Pattern) + 1 prevents the window from overflowing.
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

# Real data test for PatternCount (Vibrio cholerae / Cholera Bacterium OriC region):
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
Pattern = "TGATCA"
# Expected result is 8:
# print(PatternCount(Text, Pattern))


# ==========================================
# 3. REVERSE (String Reversal Functions)
# ==========================================

# Reverses a given DNA string completely from end to beginning.
# Converts letters to uppercase, iterates backwards into a list, and joins them.
def Reverse(Pattern):
    reve = []
    Pattern = Pattern.upper()
    for i in range(len(Pattern)-1, -1, -1):
        frag = Pattern[i:i+1]
        reve.append(frag)
    return ''.join(reve)

# Test input for Reverse:
Test_Pattern = "AAAACCCGGT"
# Expected output is "TGGCCCAAAA":
# print(Reverse(Test_Pattern))


# Alternative and Simpler Reverse Method:
# Loops through characters one by one and prepends each new character to the front.
def Reverse_Simple(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev


# ==========================================
# 4. TOP-DOWN PROGRAMMING TEMPLATE
# ==========================================

# A core architecture function that breaks down a complex problem (finding reverse complement)
# into smaller pieces (sub-functions) instead of trying to solve it all at once.
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)      # First, reverse the string (The function we wrote)
    Pattern = Complement(Pattern)   # Then, complement the nucleotides (A-T, C-G) (To be added later)
    return Pattern
# ==========================================
# 5. COMPLEMENT FUNCTION (Nucleotide Pairing)
# ==========================================

# Finds the complement of each nucleotide in the DNA string (A->T, T->A, C->G, G->C).
def Complement(Pattern):
    # Define pairing rules in a dictionary
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                       'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    
    # Replace each character with its corresponding nucleotide and join them
    complemented_list = [complement_dict.get(char, char) for char in Pattern]
    return ''.join(complemented_list)


# ==========================================
# 6. COMPLETED REVERSECOMPLEMENT ARCHITECTURE
# ==========================================

# Now that the sub-functions are ready, our main function will work seamlessly:
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)      # Step 1: Reverse the string
    Pattern = Complement(Pattern)   # Step 2: Complement the nucleotides
    return Pattern

# Let's test it:
# Test_Pattern = "AGTCGCATAGT"
# print("Reverse Complement Result:", ReverseComplement(Test_Pattern))
# Expected output: "ACTATGCGACT"
