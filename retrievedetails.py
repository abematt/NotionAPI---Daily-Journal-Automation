import json

def retrieve_details():
    file = open('SECRET.json')
    title_file = open('COUNTER.json')
    title_data = json.load(title_file)
    data = json.load(file)

    day_counter = title_data["Day"]
    journal_title = title_data["Journal_Title"]
    habit_tracker_title = title_data["Habit_Tracker_Title"]

    token = data['id']
    journalid = data['journal']
    habitid = data['habit_tracker']
    monthid = data['monthID']
    weekid = data['weekID']
    database_url = data['databaseURL']
    page_url = data["pageURL"]

    file.close()
    title_file.close()

    return token,journalid,habitid,monthid,weekid,database_url,page_url,day_counter,journal_title,habit_tracker_title