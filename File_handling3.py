#Write Python Program to Find the Longest Word in a File. Get the File Name from User. 
file = open('file1.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words in the file :', len(per_word))
max = 0
for i in read_data.split():
  if len(i) > max:
    max = len(i)
    word = i
    print(word)

print("the longest word is", word , "and its length is:", max)