# Python code to find total words in the file and length of each word
f1 = open("file1.txt",'r')
data = f1.read()
#data1 = f1.readline()
for i in data.split():
  print(i[::-1],end = ' ')
  
file = open('file1.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words in the file :', len(per_word))
for i in read_data.split():
  print(i, len(i))