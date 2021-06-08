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
get_epic_eaedate,
get_epic_id_col,
get_epic_id_npos,
get_story_id_col,
get_story_id_npos,
get_sprint_id_col,
get_sprint_id_npos,
get_story_desc_col,
get_story_desc_npos,
get_assigned_to_col,
get_assigned_to_npos,
get_esti_story_points_col,
get_esti_story_points_npos,
get_story_planned_start_col,
get_story_planned_start_npos,
get_story_planned_end_col,
get_story_planned_end_npos,
get_esti_effort_in_hrs_col,
get_esti_effort_in_hrs_npos,
get_time_spent_in_sec_col,
get_time_spent_in_sec_npos,
get_effort_cons_in_hrs_col,
get_effort_cons_in_hrs_npos,
get_pending_effort_in_hrs_col,
get_pending_effort_in_hrs_npos,
get_story_actual_start_col,
get_story_actual_start_npos,
get_story_actual_end_col,
get_story_actual_end_npos,
get_story_effort_comp_col,
get_story_effort_comp_npos

)

ik_pos = get_issue_key_pos()
ii_pos = get_issue_id_pos()
cfl_pos = get_custom_field_link_pos()
en_pos = get_ename_pos()
a_pos = get_assignee_pos()
oe_pos = get_orig_esti_pos() 
p_pos = get_progress_pos()
cfp_pos = get_custom_field_points_pos()
sh_pos = get_spenthours_pos()
re_pos = get_rem_esti_pos()
es_pos = get_esdate_pos()
et_pos = get_etdate_pos()
eas_pos = get_easdate_pos() 
eae_pos = get_eaedate_pos()
oh_pos = get_originalhours_pos()
rh_pos = get_remaininghours_pos()
ts_pos = get_time_spent_pos()
s1_pos = get_sprint_pos()
s2_pos = get_sprint2_pos()
s3_pos = get_sprint3_pos()
s_pos = get_summary_pos()
sno_pos = get_sno_pos()
epic_cfl = get_epic_custom_field_link()
epic_en_pos = get_epic_ename()
epic_es_pos = get_epic_esdate()
epic_et_pos = get_epic_etdate()
epic_eas_pos = get_epic_easDate()
epic_eae_pos = get_epic_eaedate()
ei_col = get_epic_id_col()
ei_npos = get_epic_id_npos()
si_col = get_story_id_col()
si_npos = get_story_id_npos()
sprint_id_col = get_sprint_id_col()
sprint_id_npos = get_sprint_id_npos()
sd_col = get_story_desc_col()
sd_npos = get_story_desc_npos()
at_col = get_assigned_to_col()
at_npos = get_assigned_to_npos()
esp_col = get_esti_story_points_col()
esp_npos = get_esti_story_points_npos()
sps_col = get_story_planned_start_col()
sps_npos = get_story_planned_start_npos()
spe_col = get_story_planned_end_col()
spe_npos = get_story_planned_end_npos()
ee_in_hrs_col = get_esti_effort_in_hrs_col()
ee_in_hrs_npos = get_esti_effort_in_hrs_npos()
ec_in_hrs_col = get_effort_cons_in_hrs_col()
ec_in_hrs_npos = get_effort_cons_in_hrs_npos()
ts_in_sec_col = get_time_spent_in_sec_col()
ts_in_sec_npos = get_time_spent_in_sec_npos()
pe_in_hrs_col = get_pending_effort_in_hrs_col()
pe_in_hrs_npos = get_pending_effort_in_hrs_npos()
sas_col = get_story_actual_start_col()
sas_npos = get_story_actual_start_npos()
sae_col = get_story_actual_end_col()
sae_npos = get_story_actual_end_npos()
sec_col = get_story_effort_comp_col()
sec_npos = get_story_effort_comp_npos()
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
        data[i][oh_pos] = round(int(data[i][oe_pos])/3600)
        data[i][sh_pos] = round(int(data[i][ts_pos])/3600)
        data[i][rh_pos] = round(int(data[i][re_pos])/3600)
        data[i][p_pos] = round((int(data[i][sh_pos]) / int(data[i][oh_pos]))*100)
    return data
def get_col_name(file):
	
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


def sort_sprint_data(datalines):
    for i in range(1, len(datalines)):
        s1 = datalines[i][s1_pos]
        s2 = datalines[i][s2_pos]
        s3 = datalines[i][s3_pos]

        list = [s1, s2, s3]
        list.sort(reverse = True)
        datalines[i][s1_pos] = list[s1]
        datalines[i][s2_pos] = list[s2]
        datalines[i][s3_pos] = list[s3]
    print(datalines)



        
	
def main():
    epics = "01-epics.csv"
    stories = "02-stories.csv"

    epics_data = open_file_by_filename(epics)

    stories_data = open_file_by_filename(stories) 
    set_stories_data = set_data_into_file(epics_data, stories_data)

    stories_col = get_col_name(set_stories_data)
    set_data = process_stories_data(stories_col)
    #generated_data = sort_sprint_data(set_data) 
 
    
    with open("gdata.csv", "w") as csv_file:
        gd = csv.writer(csv_file)
        for line in set_data:
            gd.writerow(line)
if (__name__ == "__main__"):
    main()



