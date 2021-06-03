import csv

def get_file_by_name(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        data_list.append(row)
    fd.close()
    return (data_list)


def operate_csv_file(data_list1, data_list2):
    n1 = len(data_list1)
    n2 = len(data_list2)
    # print(n1, n2)
    for i in range(1, n1):
        # print(i)
        for j in range(1, n2):
            # print(j)
            if data_list1[i][1] == data_list2[j][3]:
                data_list2[j][4] = data_list1[i][3]
                data_list2[j][5] = data_list1[i][4]
                data_list2[j][6] = data_list1[i][5]
                data_list2[j][7] = data_list1[i][6]
       
    return data_list2

def main():
    filename1 = "01-epics.csv"
    filename2 = "02-stories.csv"

    data_list1 = get_file_by_name(filename1)
    # print(data_list1)
    data_list2 = get_file_by_name(filename2)
    # print(data_list2)
    dlist = operate_csv_file(data_list1, data_list2)
    # print(dlist)
    glist = []
    for r in dlist:
        #print(r)
        list = ('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17]))
        glist.append(list)
    print(glist)

    with open("generated_data.csv", "w") as csv_file:
        gd = csv.writer(csv_file, delimiter = '\t')
        for line in glist:
            gd.writerow(line)

if (__name__ == "__main__"):
    main()

    
