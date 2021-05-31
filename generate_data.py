import csv
import json

def get_data_from_csv_file(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        data_list.append(row)
        row2 = row[2]
        row3 = row[3]
        print(row2, row3)
    

    fd.close()
    return data_list

def get_hours_from_sec(data_list):
    listlen = len(data_list)
    
    for i in range(1, len(data_list)):
        data_list[i][3] = (int(data_list[i][2]))/(60*60)
        data_list[i][5] = (int(data_list[i][4]))/(60*60)
        data_list[i][6] = (int(data_list[i][2])) - (int(data_list[i][4]))
        data_list[i][7] = (int(data_list[i][3]) - int(data_list[i][5]))
        data_list[i][8] = (int(data_list[i][4])/int(data_list[i][2])) * 100
        '''     
        if (data_list[i][3] == "0"):
            hrs = (int(data_list[i][2]))/(60*60)
            hr = str(hrs)
            print(hr)
        '''
    return(data_list)


def main():
    filename = "02-data.csv"
    data_list = get_data_from_csv_file(filename)
    print(data_list)
    dlist = get_hours_from_sec(data_list)
    print("dlist:",dlist)

    with open("guser-data.csv", "w") as csv_file:

        gd = csv.writer(csv_file, delimiter = '\t')
        for line in dlist:
            gd.writerow(line)


if (__name__ == "__main__"):
    main()
    
