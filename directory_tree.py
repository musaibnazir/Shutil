import os
for folderName, subfolders, filename in os.walk(''):
    print('' + folderName)

    for subfolder in subforders:
        print(''+folderName+':'+subfolder)

    for filename in filenames:
        print(''+folderName+':'+filename)

    print('')    
