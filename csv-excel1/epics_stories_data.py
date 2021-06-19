from openpyxl import load_workbook

story_to_columns = {
	"s.no":{"pos": 0},
	"Issue key":{"pos": 1, "gen_pos": {"gcol_name": "STORY ID", "npos": 3}},
	"Issue id": {"pos": 2},
	"Custom field (Epic Link)": {"pos": 3, "gen_pos": {"gcol_name": "EPIC ID", "npos":1}},
	"Ename":{"pos": 4},
	
	"Assignee":{"pos":5, "gen_pos": {"gcol_name": "ASSIGNED TO", "npos": 5}},
	
	"Custom field (Story Points)":{"pos":6, "gen_pos": {"gcol_name": "ESTIMATED\nSTORY\nPOINTS", "npos": 6}},
	"Original Estimate":{"pos":8,"gen_pos": {"gcol_name": "Time spent\n(IN Secs)", "npos": 10 }},

        "Time Spent": {"pos": 9},
        "Remaining Estimate":{"pos":10},
        "Sprint":{"pos":11, "gen_pos": {"gcol_name": "SPRINT ID", "npos": 2}},
        "Sprint2":{"pos":12},
        "Sprint3":{"pos":13},
        "Summary":{"pos": 14, "gen_pos": {"gcol_name": "STORY DESCRIPTION", "npos": 4}},
		"originalhours": {"gen_pos": {"gcol_name": "EFFORT\nCONSUMED\n(IN HRS)", "npos": 11 }},
		"spenthours": {"gen_pos": {"gcol_name": "ESTIMATED\nEFFORT\n(IN HRS))", "npos": 9}},
		"remaininghours": {"gen_pos": {"gcol_name": "PENDING\nEFFORT\n(IN HRS)", "npos":12}},
		"progress":{"gen_pos": {"gcol_name":"STORY\nEffort\ncompletion\n%", "npos": 15}},
        "story_schedule_progress":{"gen_pos": {"gcol_name" : "STORY\nSchedule\nProgress % ","npos": 16}},
        "story_schedule_overrun":{"gen_pos": {"gcol_name": "STORY\nSchedule\nOverrun %", "npos": 17}},
	"remarks": {"gen_pos": {"gcol_name": "Remarks", "npos": 18}}
}
epics_to_columns = {
	"s.no": {"pos":0},
	"Custom field (Epic Link)": {"pos": 1},
	"Ename": {"pos": 2},
	"ESdate":{"pos":3, "gen_pos": {"gcol_name": "STORY\nPLANNED\nSTART", "npos": 7}},
	"ETdate":{"pos": 4, "gen_pos": {"gcol_name":"STORY\nPLANNED\nEND", "npos": 8}},
	"EASdate":{"pos": 5, "gen_pos": {"gcol_name":"STORY\nACTUAL\nSTART", "npos": 13}},
	"EAEdate":{"pos": 6,"gen_pos": {"gcol_name":"STORY\nACTUAL\nEND", "npos": 14}},
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

def get_assignee_pos():
    return story_to_columns["Assignee"]["pos"]
def get_progress_pos():
    return story_to_columns["progress"]["pos"]
def get_custom_field_points_pos():
    return story_to_columns["Custom field (Story Points)"]["pos"]

def get_orig_esti_pos():
    return story_to_columns["Original Estimate"]["pos"]


def get_time_spent_pos():
    return story_to_columns["Time Spent"]["pos"]


def get_rem_esti_pos():
    return story_to_columns["Remaining Estimate"]["pos"]


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
    return epics_to_columns["EASdate"]["pos"]
def get_epic_eaedate():
    return epics_to_columns["EAEdate"]["pos"]


	
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
    return epics_to_columns["ESdate"]["gen_pos"]["gcol_name"]
def get_story_planned_start_npos():
    return epics_to_columns["ESdate"]["gen_pos"]["npos"]
def get_story_planned_end_col():
    return epics_to_columns["ETdate"]["gen_pos"]["gcol_name"]
def get_story_planned_end_npos():
    return epics_to_columns["ETdate"]["gen_pos"]["npos"]
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
    return epics_to_columns["EASdate"]["gen_pos"]["gcol_name"]
def get_story_actual_start_npos():
    return epics_to_columns["EASdate"]["gen_pos"]["npos"]
def get_story_actual_end_col():
    return epics_to_columns["EAEdate"]["gen_pos"]["gcol_name"]
def get_story_actual_end_npos():
    return epics_to_columns["EAEdate"]["gen_pos"]["npos"]
def get_story_effort_comp_col():
    return story_to_columns["progress"]["gen_pos"]["gcol_name"]
def get_story_effort_comp_npos():
    return story_to_columns["progress"]["gen_pos"]["npos"]
def get_story_schedule_progress_col():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["gcol_name"]
def get_story_schedule_progress_npos():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["npos"]
def get_story_schedule_overrun_pos():
    return story_to_columns["story_schedule_overrun"]["pos"]
def get_story_schedule_overrun_col():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["gcol_name"]
def get_story_schedule_overrun_npos():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["npos"]
def get_remarks_col():
    return story_to_columns["remarks"]["gen_pos"]["gcol_name"]
def get_remarks_npos():
    return story_to_columns["remarks"]["gen_pos"]["npos"]
	

    


