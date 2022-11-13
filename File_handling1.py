# Python code to reverse each word of text file
f1 = open("file1.txt",'r')
data = f1.read()
for i in data.split():
  print(i[::-1],end = ' ')