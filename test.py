longest,shortest='','anyLargeWordWillWorkForThisString'
myfile = open('test.txt','w')
line = input("Enter 5-6 lines:")
myfile.write(line)
myfile.close()
myfile = open('test.txt','r')
lines = myfile.read()
lines = lines.split()
for i in range(len(lines)):
    if len(lines[i])>len(longest):
        longest=lines[i]
    elif len(lines[i])<len(shortest):
        shortest=lines[i]
    else:
        pass
print("longest word is:",longest)
print("Shortest word is:", shortest)
print('Length of longest word',len(longest))
print('Length of shortest word',len(shortest))
myfile.close()