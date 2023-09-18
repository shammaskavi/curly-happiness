# String similarity 
import difflib

def findSimilarity(s1,s2):
    d = difflib.SequenceMatcher(None, s1.lower(), s2.lower())
    return d.ratio()

s1 = input("Input String 1: ")
s2 = input("Input String 2: ")
similarityIndex = findSimilarity(s1,s2)

if similarityIndex == 1:
    print(f"The String are similar with the similarity index of {similarityIndex}")
else:
    print(f"The string are not similar with the similarity index of {similarityIndex}")