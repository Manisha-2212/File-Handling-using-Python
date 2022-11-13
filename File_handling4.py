#Write Python Program to Count the Occurrences of Each Word in a “file1.txt” File.
counts = dict()
f1 = open("file1.txt",'r')
data = f1.read()
for i in data.split():
  if i in counts:
    counts[i] += 1
  else:
    counts[i] = 1

print(counts) 