story_to_columns = {
	"s.no":{"pos": 0},
	"Issue key":{"pos": 1},
	"Issue id": {"pos": 2},
	"Custom field (Epic Link)": {"pos": 3},
	"Ename":{"pos": 4},
	"ESdate":{"pos":5},
	"ETdate":{"pos": 6},
	"EASdate":{"pos": 7},
	"EAEdate":{"pos": 8},
	"Assignee":{"pos":9},
	"progress":{"pos":10},
	"Custom field (Story Points)":{"pos":11},
	"Original Estimate":{"pos":12},
	"originalhours": {"pos": 13},
	"Time Spent": {"pos": 14},
	"spenthours": {"pos":15},
	"Remaining Estimate":{"pos":16},
	"remaininghours": {"pos": 17},
	"Sprint":{"pos":18},
	"Sprint2":{"pos":19},
	"Sprint3":{"pos":20},
	"Summary":{"pos": 21}
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
def s_no_pos():
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
   return story_to_columns["Sprint"]["pos"]

def get_sprint3_pos():
    return story_to_columns["Sprint"]["pos"]
	
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
