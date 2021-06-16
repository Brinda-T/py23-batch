from openpyxl import load_workbook

story_to_columns = {
	"s.no":{"pos": 0},
	"Issue key":{"pos": 1, "gen_pos": {"gcol_name": "STORY ID", "npos": 3}},
	"Issue id": {"pos": 2},
	"Custom field (Epic Link)": {"pos": 3, "gen_pos": {"gcol_name": "EPIC ID", "npos":1}},
	"Ename":{"pos": 4},
	"ESdate":{"pos":5, "gen_pos": {"gcol_name": "STORY\nPLANNED\nSTART", "npos": 7}},
	"ETdate":{"pos": 6, "gen_pos": {"gcol_name":"STORY\nPLANNED\nEND", "npos": 8}},
	"EASdate":{"pos": 7, "gen_pos": {"gcol_name":"STORY\nACTUAL\nSTART", "npos": 13}},
	"EAEdate":{"pos": 8,"gen_pos": {"gcol_name":"STORY\nACTUAL\nEND", "npos": 14}},
	"Assignee":{"pos":9, "gen_pos": {"gcol_name": "ASSIGNED TO", "npos": 5}},
	"progress":{"pos":10,"gen_pos": {"gcol_name":"STORY\nEffort\ncompletion\n%", "npos": 15}},
	"Custom field (Story Points)":{"pos":11, "gen_pos": {"gcol_name": "ESTIMATED\nSTORY\nPOINTS", "npos": 6}},
	"Original Estimate":{"pos":12,"gen_pos": {"gcol_name": "Time spent\n(IN Secs)", "npos": 10 }},
        "originalhours": {"pos": 13, "gen_pos": {"gcol_name": "EFFORT\nCONSUMED\n(IN HRS)", "npos": 11 }},
        "Time Spent": {"pos": 14},
        "spenthours": {"pos":15, "gen_pos": {"gcol_name": "ESTIMATED\nEFFORT\n(IN HRS))", "npos": 9}},
        "Remaining Estimate":{"pos":16},
        "remaininghours": {"pos": 17, "gen_pos": {"gcol_name": "PENDING\nEFFORT\n(IN HRS)", "npos":12}},
        "Sprint":{"pos":18, "gen_pos": {"gcol_name": "SPRINT ID", "npos": 2}},
        "Sprint2":{"pos":19},
        "Sprint3":{"pos":20},
        "Summary":{"pos": 21, "gen_pos": {"gcol_name": "STORY DESCRIPTION", "npos": 4}},
        "story_schedule_progress":{"pos": 22, "gen_pos": {"gcol_name" : "STORY\nSchedule\nProgress % ","npos": 16}},
        "story_schedule_overrun":{"pos": 23, "gen_pos": {"gcol_name": "STORY\nSchedule\nOverrun %", "npos": 17}},
	"remarks": {"pos": 24, "gen_pos": {"gcol_name": "Remarks", "npos": 18}}
}
epics_to_columns = {
	"s.no": {"pos":0},
	"Custom field (Epic Link)": {"pos": 1},
	"Ename": {"pos": 2},
	"ESdate": {"pos":3},
	"ETdate":{"pos":4},
	"EASDate": {"pos":5},
	"EAEDate": {"pos": 6}
}
def get_s_no_pos():
    return story_to_columns["s.no"]["pos"]

def get_issue_key_pos():
    return story_to_columns["Issue key"]["pos"]

def get_issue_id_pos():
    return story_to_columns["Issue id"]["pos"]

def get_custom_field_link_pos():
    return story_to_columns["Custom field (Epic Link)"]["pos"]
def get_ename_pos():
    return story_to_columns["Ename"]["pos"]
def get_esdate_pos():
    return story_to_columns["ESdate"]["pos"]
def get_etdate_pos():
    return story_to_columns["ETdate"]["pos"]
def get_easdate_pos():
    return story_to_columns["EASdate"]["pos"]
def get_eaedate_pos():
    return story_to_columns["EAEdate"]["pos"]

def get_assignee_pos():
    return story_to_columns["Assignee"]["pos"]
def get_progress_pos():
    return story_to_columns["progress"]["pos"]
def get_custom_field_points_pos():
    return story_to_columns["Custom field (Story Points)"]["pos"]

def get_orig_esti_pos():
    return story_to_columns["Original Estimate"]["pos"]

def get_originalhours_pos():
    return story_to_columns["originalhours"]["pos"]
def get_time_spent_pos():
    return story_to_columns["Time Spent"]["pos"]

def get_spenthours_pos():
    return story_to_columns["spenthours"]["pos"]
def get_rem_esti_pos():
    return story_to_columns["Remaining Estimate"]["pos"]

def get_remaininghours_pos():
    return story_to_columns["remaininghours"]["pos"]
def get_sprint_pos():
    return story_to_columns["Sprint"]["pos"]

def get_sprint2_pos():
   return story_to_columns["Sprint2"]["pos"]

def get_sprint3_pos():
    return story_to_columns["Sprint3"]["pos"]
	
def get_summary_pos():
    return story_to_columns["Summary"]["pos"]
	

def get_sno_pos():
    return epics_to_columns["s.no"]["pos"]
def get_epic_custom_field_link():
    return epics_to_columns["Custom field (Epic Link)"]["pos"]
def get_epic_ename():
    return epics_to_columns["Ename"]["pos"]
def get_epic_esdate():
    return epics_to_columns["ESdate"]["pos"]
def get_epic_etdate():
    return epics_to_columns["ETdate"]["pos"]
def get_epic_easDate():
    return epics_to_columns["EASDate"]["pos"]
def get_epic_eaedate():
    return epics_to_columns["EAEDate"]["pos"]
	
def get_epic_id_col():
    return story_to_columns["Custom field (Epic Link)"]["gen_pos"]["gcol_name"]
def get_epic_id_npos():
    return story_to_columns["Custom field (Epic Link)"]["gen_pos"]["npos"]
def get_story_id_col():
    return story_to_columns["Issue key"]["gen_pos"]["gcol_name"]
def get_story_id_npos():
    return story_to_columns["Issue key"]["gen_pos"]["npos"]
def get_sprint_id_col():
    return story_to_columns["Sprint"]["gen_pos"]["gcol_name"]
def get_sprint_id_npos():
    return story_to_columns["Sprint"]["gen_pos"]["npos"]
def get_story_desc_col():
    return story_to_columns["Summary"]["gen_pos"]["gcol_name"]
def get_story_desc_npos():
    return story_to_columns["Summary"]["gen_pos"]["npos"]
def get_assigned_to_col():
    return story_to_columns["Assignee"]["gen_pos"]["gcol_name"]
def get_assigned_to_npos():
    return story_to_columns["Assignee"]["gen_pos"]["npos"]
def get_esti_story_points_col():
    return story_to_columns["Custom field (Story Points)"]["gen_pos"]["gcol_name"]
def get_esti_story_points_npos():
    return story_to_columns["Custom field (Story Points)"]["gen_pos"]["npos"]
def get_story_planned_start_col():
    return story_to_columns["ESdate"]["gen_pos"]["gcol_name"]
def get_story_planned_start_npos():
    return story_to_columns["ESdate"]["gen_pos"]["npos"]
def get_story_planned_end_col():
    return story_to_columns["ETdate"]["gen_pos"]["gcol_name"]
def get_story_planned_end_npos():
    return story_to_columns["ETdate"]["gen_pos"]["npos"]
def get_esti_effort_in_hrs_col():
    return story_to_columns["spenthours"]["gen_pos"]["gcol_name"]
def get_esti_effort_in_hrs_npos():
    return story_to_columns["spenthours"]["gen_pos"]["npos"]
def get_time_spent_in_sec_col():
    return story_to_columns["Original Estimate"]["gen_pos"]["gcol_name"]
def get_time_spent_in_sec_npos():
    return story_to_columns["Original Estimate"]["gen_pos"]["npos"]

def get_effort_cons_in_hrs_col():
    return story_to_columns["originalhours"]["gen_pos"]["gcol_name"]
def get_effort_cons_in_hrs_npos():
    return story_to_columns["originalhours"]["gen_pos"]["npos"]
def get_pending_effort_in_hrs_col():
    return story_to_columns["remaininghours"]["gen_pos"]["gcol_name"]
def get_pending_effort_in_hrs_npos():
    return story_to_columns["remaininghours"]["gen_pos"]["npos"]
def get_story_actual_start_col():
    return story_to_columns["EASdate"]["gen_pos"]["gcol_name"]
def get_story_actual_start_npos():
    return story_to_columns["EASdate"]["gen_pos"]["npos"]
def get_story_actual_end_col():
    return story_to_columns["EAEdate"]["gen_pos"]["gcol_name"]
def get_story_actual_end_npos():
    return story_to_columns["EAEdate"]["gen_pos"]["npos"]
def get_story_effort_comp_col():
    return story_to_columns["progress"]["gen_pos"]["gcol_name"]
def get_story_effort_comp_npos():
    return story_to_columns["progress"]["gen_pos"]["npos"]
def get_story_schedule_progress_pos():
    return story_to_columns["story_schedule_progress"]["pos"]
def get_story_schedule_progress_col():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["gcol_name"]
def get_story_schedule_progress_npos():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["npos"]
def get_story_schedule_overrun_npos():
    return story_to_columns["story_schedule_overrun"]["pos"]
def get_story_schedule_overrun_pos():
    return story_to_columns["story_schedule_overrun"]["pos"]
def get_story_schedule_overrun_col():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["gcol_name"]
def get_story_schedule_overrun_npos():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["npos"]
def get_remarks_pos():
    return story_to_columns["remarks"]["pos"]
def get_remarks_col():
    return story_to_columns["remarks"]["gen_pos"]["gcol_name"]
def get_remarks_npos():
    return story_to_columns["remarks"]["gen_pos"]["npos"]
	

def get_colnames_with_pos(wbname, src_wname, dst_wname):

    worksheet = []
    wb = load_workbook(wbname)    
    swsheet = wb.get_sheet_by_name(src_wname)
    try:
        dwsheet = wb.get_sheet_by_name(dst_wname)
        print("Worksheet '%s' found" %(dst_wname))

        print("Removing worksheet: '%s'" %(dst_wname))
        wb.remove_sheet(dst_wname)
    except:
        print("Worksheet '%s' not found" %(dst_wname))
        dwsheet = wb.create_sheet(dst_wname)

    srcount = swsheet.max_row
    sccount = swsheet.max_column

    drcount = dwsheet.max_row
    dccount = dwsheet.max_column
    
    dwsheet.insert_cols(1,19)
    for i in range(1, srcount+1):
        print(swsheet[i][cfl_pos].value)
        dwsheet[i][sno_pos].value = swsheet[i][sno_pos].value
        dwsheet[i][ei_npos].value = swsheet[i][cfl_pos].value
        dwsheet[i][sprint_id_npos].value = swsheet[i][s1_pos].value
        dwsheet[i][si_npos].value = swsheet[i][ik_pos].value
        dwsheet[i][sd_npos].value = swsheet[i][s_pos+3].value
        dwsheet[i][at_npos].value = swsheet[i][a_pos].value
        dwsheet[i][esp_npos].value = swsheet[i][cfp_pos].value
        dwsheet[i][sps_npos].value = swsheet[i][es_pos].value
        dwsheet[i][sae_npos].value = swsheet[i][et_pos].value
        dwsheet[i][ee_in_hrs_npos].value = swsheet[i][oh_pos].value
        dwsheet[i][ts_in_sec_npos].value = swsheet[i][oe_pos].value
        dwsheet[i][ec_in_hrs_npos].value = swsheet[i][oh_pos].value
        dwsheet[i][pe_in_hrs_npos].value = swsheet[i][rh_pos].value
        dwsheet[i][sas_npos].value = swsheet[i][eas_pos].value
        dwsheet[i][sae_npos].value = swsheet[i][eae_pos].value
        dwsheet[i][sec_npos].value = swsheet[i][p_pos].value
        dwsheet[i][ssp_npos].value = swsheet[i][ssp_pos-1].value
        dwsheet[i][sso_npos].value = swsheet[i][sso_pos-1].value
        dwsheet[i][r_npos].value = swsheet[i][r_pos-1].value
    '''
    for row in swsheet.iter_rows():
        if(row[2].value != None):
            frow = [cell.value for cell in row]
            dwsheet.append(frow)
    
    for i in range(2, srcount+1):
        s1 = swsheet[i][s1_pos].value
        s2 = swsheet[i][s2_pos].value
        s3 = swsheet[i][s3_pos].value

        t = [s1, s2, s3]
        t.sort(reverse = True)
        
        
        dwsheet[i][s1_pos].value = t[0]
        dwsheet[i][s2_pos].value = t[1]
        dwsheet[i][s3_pos].value = t[2]
    dwsheet[1][cfl_pos].value = ei_col
    dwsheet[1][ik_pos].value = si_col
    dwsheet[1][s1_pos].value = sprint_id_col
    dwsheet[1][s_pos].value = sd_col
    dwsheet[1][a_pos].value = at_col
    dwsheet[1][cfp_pos].value = esp_col
    dwsheet[1][es_pos].value = sps_col
    dwsheet[1][et_pos].value = spe_col
    dwsheet[1][sh_pos].value = ee_in_hrs_col
    dwsheet[1][oe_pos].value = ts_in_sec_col
    dwsheet[1][oh_pos].value = ec_in_hrs_col
    dwsheet[1][rh_pos].value = pe_in_hrs_col
    dwsheet[1][eas_pos].value = sas_col
    dwsheet[1][eae_pos].value = sae_col
    dwsheet[1][p_pos].value = sec_col
    dwsheet.insert_cols(ssp_npos)
    dwsheet.insert_cols(sso_npos)
    print(ssp_npos)
    print(dwsheet[1][21].value)
    dwsheet[1][ssp_npos-1].value = ssp_col
    dwsheet[1][sso_npos-1].value = sso_col
    for j in range (2, srcount+1):
        
        dwsheet[j][ssp_npos-1].value = "100%"
        dwsheet[j][sso_npos-1].value = "0%"
    
    for j in range(0, 24):
        print(j, dwsheet[1][j].value)

    for i in range(1, srcount+1):
        list = [dwsheet[i][sno_pos].value,dwsheet[i][cfl_pos].value, dwsheet[i][s1_pos].value, dwsheet[i][ik_pos].value, dwsheet[i][s_pos+2].value, dwsheet[i][a_pos].value, dwsheet[i][cfp_pos].value, dwsheet[i][es_pos].value, 
                dwsheet[i][et_pos].value, dwsheet[i][oh_pos].value, dwsheet[i][oe_pos].value, dwsheet[i][oh_pos].value, dwsheet[i][rh_pos].value, dwsheet[i][eas_pos].value,
                dwsheet[i][eae_pos].value, dwsheet[i][p_pos].value, dwsheet[i][ssp_npos].value, dwsheet[i][sso_npos].value]
        worksheet.append(list)
    
    
    	
    '''
    wb.save(wbname)		
		
    
sno_pos = get_s_no_pos()
ik_pos =get_issue_key_pos()
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
ssp_pos = get_story_schedule_progress_pos()
ssp_col = get_story_schedule_progress_col()
ssp_npos = get_story_schedule_progress_npos()
sso_pos = get_story_schedule_overrun_pos()
sso_col = get_story_schedule_overrun_col()
sso_npos = get_story_schedule_overrun_npos()
r_pos = get_remarks_pos()
r_col = get_remarks_col()
r_npos = get_remarks_npos()

def main():
    wbook = "generate-files.xlsx"
    src_wsheet ="epic_stories"
    dst_wsheet = "gen_sheet"
    get_colnames_with_pos(wbook, src_wsheet, dst_wsheet)

if (__name__ == "__main__"):
    main()
