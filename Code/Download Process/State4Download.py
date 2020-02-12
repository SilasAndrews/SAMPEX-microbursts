import urllib.request as ur
import zipfile as zp
import os

state4 = open("State4Links.txt", "r")

for line in state4:
    pair = line.split(" ")
    name = pair[0]
    url = pair[1][:-1]
    
    if 'zip' not in url:
        ur.urlretrieve(url, name)
    else:
        name = name + ".zip"
        ur.urlretrieve(url, name)
        with zp.ZipFile(name, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall()
        os.remove(name)
    

state4.close()



