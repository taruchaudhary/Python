fw = open('sample.txt','w')
fw.write('writing  some stuff in my text file\n')
fw.write('i like book\n')
fw.close()

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()


