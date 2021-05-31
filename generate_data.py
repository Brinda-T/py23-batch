import csv
import json
import math

def get_data_from_csv_file(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        data_list.append(row)

    fd.close()
    return data_list

def get_hours_from_sec(data_list):
    listlen = len(data_list)
    
    for i in range(1, len(data_list)):
        data_list[i][3] = math.ceil((int(data_list[i][2]))/(60*60))
        data_list[i][5] = math.ceil((int(data_list[i][4]))/(60*60))
        data_list[i][6] = math.ceil((int(data_list[i][2])) - (int(data_list[i][4])))
        data_list[i][7] = math.ceil((int(data_list[i][3]) - int(data_list[i][5])))
        data_list[i][8] = math.ceil((int(data_list[i][4])/int(data_list[i][2])) * 100)
    
    return(data_list)


def main():
    filename = "02-data.csv"
    data_list = get_data_from_csv_file(filename)
    print(data_list)
    dlist = get_hours_from_sec(data_list)
    print("dlist:",dlist)
    glist = []
    for r in dlist:
        list = ('{},{},{},{},{},{},{},{},{}'.format(r[0],r[1],r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        glist.append(list)
    print(glist)

    with open("guser-data.csv", "w") as csv_file:

        gd = csv.writer(csv_file, delimiter = '\t')
        for line in glist:
            gd.writerow(line)


if (__name__ == "__main__"):
    main()
    
