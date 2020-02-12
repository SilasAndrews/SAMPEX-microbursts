import urllib.request as ur
import zipfile as zp
import os


def main(input_file):

    with open(input_file, "r") as state:

        for line in state:
            pair = line.split(" ")
            name = pair[0]
            url = pair[1][:-1]
            path = input_file[:7] + name
            folder = input_file[:7]

            if 'zip' not in url:
                ur.urlretrieve(url, path)
            else:
                path = path + ".zip"
                ur.urlretrieve(url, path)
                with zp.ZipFile(path, 'r') as zipObj:
                    # Extract all the contents of zip file in current directory
                    zipObj.extractall(folder)
                os.remove(path)


main("Data/State1/State1Links.txt")
main("Data/State4/State4Links.txt")
