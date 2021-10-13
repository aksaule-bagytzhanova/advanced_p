#Modes
#r - opens a file for reading.
#w - opens a file for writing
#x - opens a file for exclusive creation. If the file already
#exists, the operation fails
#a - opens a file appending at the end of the file without
#truncating
#t - opens in text mode
#b - opens in binary mode
#+ opens a file for updating


#Open file
f = open("test.txt")

f = open("test.txt", mode='r', encoding='utf-8')
f.close()

try:
    f = open("test.txt", encoding='utf-8')
finally:
    f.close()

with open("test.txt", encoding= 'utf-8') as f:
    f.write('Something')

#read file

f = open("test.txt","r", encoding="utf-8")
f.read(4) #read the first 4 data

#loop read
for line in f:
    print(line, end = '')


#reads by line
f.readline()

#read all lines
f.readlines()
