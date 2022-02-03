import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        print(filename)
        os.unlink(filename)



import send2trash
baconFile = open('','')
baconFile.write('')
baconFile.close()
send2trash.send2trash('bacon.txt')
