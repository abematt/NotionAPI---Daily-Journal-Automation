import json, requests
from retrievedetails import retrieve_details
from readdatabase import readDatabase
from createhabitentry import createHabitTrackerEntry
from createjournalentry import createJournalEntry
from getidfromjson import getIdFromJson
from updatedetails import updateDateCounterDetails

updateDateCounterDetails()
token,journalID,habitID,monthID,weekID,databaseURL,pageURL,day_counter,journal_title,habit_tracker_title = retrieve_details()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}


# readDatabase(databaseURL,journalID,headers)
journal_response = createJournalEntry(headers,pageURL,journalID,monthID,weekID,day_counter,journal_title)
journal_id_created = getIdFromJson(journal_response)
habit_response = createHabitTrackerEntry(headers,pageURL,habitID,journal_id_created,habit_tracker_title)
