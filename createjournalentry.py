import json, requests

def createJournalEntry(headers,pageURL,journalID,monthID,weekID,day_counter,journal_title):
    journal_title_full = "Day " + day_counter + ": " + journal_title 
    newEntryData = {
        "parent": {"database_id": journalID},
        "properties": {
            "Week": { "id": "EsLB", "type": "relation", "relation": [{ "id":weekID}] },
            "Month": { "id": "sOKV", "type": "relation", "relation": [ { "id":monthID}] },
            "Day Counter": { "id": "~t%3BM", "type": "number", "number": int(day_counter) },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": { "content": journal_title_full, "link": None },
              "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default"
              },
              "plain_text": journal_title_full,
              "href": None
            }
                 ]
            }
                    }
                }
    data = json.dumps(newEntryData)

    response = requests.request("POST",pageURL,headers=headers,data=data)

    return response