def main(input_file):
    data_list = open(input_file, 'r')
    path = 'D:\Sample Lab\SAMPEX\DATA\State4\State4links.txt' 
    #print(path)
    links = open(path, 'w')

    for line in data_list:
        if 'zip' in line:
            file_name = line[line.index('h'):line.index('zip')+3]
            file_link = "http://www.srl.caltech.edu/sampex/DataCenter/DATA/HILThires/State4/" + file_name
            file_name = file_name[:-4]
            links.write(file_name + " " + file_link + "\n")
        else:
            file_name = line[line.index('h'):line.index('txt')+3]
            file_link = "http://www.srl.caltech.edu/sampex/DataCenter/DATA/HILThires/State4/" + file_name
            links.write(file_name + " " + file_link + "\n")
        
    data_list.close()
    links.close()

main('State4List.txt') 

