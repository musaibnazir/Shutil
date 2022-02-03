import zipfile, os
os.chdir('C:\\')
# move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()





exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()
