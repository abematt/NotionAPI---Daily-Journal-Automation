import json
from datetime import datetime
import calendar

def updateDateCounterDetails():
    
    file = open('COUNTER.json',"r+")
    data = json.load(file)
    day_counter = int(data["Day"])
    day_counter = day_counter + 1
    day_counter = str(day_counter)
    data["Day"] = day_counter
    journal_title_generated,habit_title_generated = createDateTitle()
    data["Journal_Title"] = journal_title_generated
    data["Habit_Tracker_Title"] = habit_title_generated
    file.seek(0)
    json.dump(data,file)
    file.truncate()
    file.close()


def createDateTitle():
    today = datetime.today()
    day = f"{today.day:02d}"
    year = str(today.year)
    month = f"{today.month:02d}"
    month_name = calendar.month_name[today.month]
    journal_title = month_name[:3] + '-' + day + '-' + year
    habit_title = year + "-" + month + "-" + day
    return journal_title,habit_title
