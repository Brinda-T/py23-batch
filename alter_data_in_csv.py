import csv
from stories_epics_data import( get_issue_key_pos,
get_issue_id_pos,
get_custom_field_link_pos,
get_ename_pos,
get_assignee_pos,
get_orig_esti_pos, 
get_progress_pos,
get_custom_field_points_pos,
get_spenthours_pos,
get_rem_esti_pos,
get_esdate_pos,
get_etdate_pos,
get_easdate_pos, 
get_eaedate_pos, 
get_originalhours_pos,
get_remaininghours_pos,
get_time_spent_pos,
get_sprint_pos,
get_sprint2_pos,
get_sprint3_pos,
get_summary_pos,
get_sno_pos,
get_epic_custom_field_link,
get_epic_ename,
get_epic_esdate,
get_epic_etdate,
get_epic_easDate,
get_epic_eaedate
)

def open_file_by_filename(file):
    datalist = []

    fd = open(file, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        datalist.append(row)

    fd.close()
    return datalist

def process_stories_data(data):
    for i in range(1, len(data)):
        oe_pos = get_orig_esti_pos()
        oh_pos = get_originalhours_pos()
        ts_pos = get_time_spent_pos()
        sh_pos = get_spenthours_pos()
        re_pos = get_rem_esti_pos()
        rh_pos = get_remaininghours_pos()
        p_pos = get_progress_pos()
		
        print(oe_pos)
        data[i][oh_pos] = round(int(data[i][oe_pos])/3600)
        data[i][sh_pos] = round(int(data[i][ts_pos])/3600)
        data[i][rh_pos] = round(int(data[i][re_pos])/3600)
        data[i][p_pos] = round((int(data[i][sh_pos]) / int(data[i][oh_pos]))*100)
    return data
def get_col_name(file):
    p_pos = get_progress_pos()
    oh_pos = get_originalhours_pos()
    sh_pos = get_spenthours_pos()
    rh_pos = get_remaininghours_pos()
	
    file[0].insert(p_pos,"progress")
    file[0].insert(oh_pos,"originalhours")
    file[0].insert(sh_pos,"spenthours")
    file[0].insert(rh_pos, "remaininghours")
    for j in range(1, len(file)):
        file[j].insert(p_pos, "0")
        file[j].insert(oh_pos, "0")
        file[j].insert(sh_pos, "0")
        file[j].insert(rh_pos, "0")
    return file

def set_data_into_file(file, data):
    i = 0 
    j = 0
    es_pos = get_esdate_pos()
    et_pos = get_etdate_pos()
    eas_pos = get_easdate_pos()
    eae_pos = get_eaedate_pos()
    epic_es_pos = get_epic_esdate()
    epic_et_pos = get_epic_etdate()
    epic_eas_pos = get_epic_easDate()
    epic_eae_pos = get_epic_eaedate()
    data[0].insert(es_pos,"ESdate")
    data[0].insert(et_pos,"ETdate")
    data[0].insert(eas_pos,"EASdate")
    data[0].insert(eae_pos,"EAEdate")
    for i in range(1, len(file)):
        for j in range(1, len(data)):
            if(file[i][1] == data[j][3]):
				
                data[j].insert(es_pos, file[i][epic_es_pos])
                data[j].insert(et_pos, file[i][epic_et_pos])
                data[j].insert(eas_pos, file[i][epic_eas_pos])
                data[j].insert(eae_pos, file[i][epic_eae_pos])
    return data



def main():
    epics = "01-epics.csv"
    stories = "02-stories.csv"

    epics_data = open_file_by_filename(epics)

    stories_data = open_file_by_filename(stories) 
    set_stories_data = set_data_into_file(epics_data, stories_data)

    stories_col = get_col_name(set_stories_data)
    set_data = process_stories_data(stories_col)
   
    
    with open("gdata.csv", "w") as csv_file:
        gd = csv.writer(csv_file)
        for line in set_data:
            gd.writerow(line)
if (__name__ == "__main__"):
    main()



