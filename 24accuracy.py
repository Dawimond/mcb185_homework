# 24accuracy by Yutong Ji

import math

def acc_and_f1(TP, FP, TN, FN): 
	acc = (TP + TN) / (TP + FN + TN + FP)
	f1 = (2*(TP / (TP + FP))*(TP / (TP + FN))) / \
	((TP / (TP + FP)) + (TP / (TP + FN)))
	return acc, f1

print("Example 1: TP = 120, FP = 70, TN = 40, FN = 170")
TP = 120
FP = 70
TN = 40
FN = 170
print("Accuracy & F1 Score: ", acc_and_f1(TP, FP, TN, FN))

print("Example 2: TP = 35, FP = 11, TN = 27, FN = 44")
TP = 35
FP = 11
TN = 27
FN = 44
print("Accuracy & F1 Score: ", acc_and_f1(TP, FP, TN, FN))

print("Example 3: TP = 7, FP = 9, TN = 13, FN = 4")
TP = 7
FP = 9
TN = 13
FN = 4
print("Accuracy & F1 Score: ", acc_and_f1(TP, FP, TN, FN))