# 23hydropathy.py by Yutong Ji

import sys

def AminoAcidletter(x):
	if x == "I": return 4.5
	if x == "V": return 4.2
	if x == "L": return 3.8
	if x == "F": return 2.8
	if x == "C": return 2.5
	if x == "M": return 1.9
	if x == "A": return 1.8
	if x == "G": return -0.4
	if x == "T": return -0.7
	if x == "W": return -0.9
	if x == "S": return -0.8
	if x == "Y": return -1.3
	if x == "P": return -1.6
	if x == "H": return -3.2
	if x == "E": return -3.5
	if x == "Q": return -3.5
	if x == "D": return -3.5
	if x == "N ": return -3.5
	if x == "K": return -3.9
	if x == "R": return -4.5
	sys.exit("ERROR! Unknown Amino Acid!")

print("Example 1: Proline(P)")
print("Hydrophobicity = ", aaletter("P"))

print("Example 2: Leucine(L)")
print("Hydrophobicity = ", aaletter("L"))

print("Example 3: Unknown(Z)")
print("Hydrophobicity = ", aaletter("Z"))