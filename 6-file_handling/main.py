import os.path
import sys

fname = input("Enter the filename : ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(1)


with open(fname, "r") as infile:
    lineList = infile.readlines()
    print(len(lineList))

for i in range(len(lineList)):
    print(i + 1, ":", lineList[i])

word = input("Enter a word : ")
count = 0

for line in lineList:
    count += line.count(word)


print("The word", word, "appears", count, "times in the file")
