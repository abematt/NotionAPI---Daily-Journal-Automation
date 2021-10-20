import json, requests

def createHabitTrackerEntry(headers,pageURL,habitID,journal_id_created,habit_tracker_title):
  newEntryData = {
      "parent": {"database_id": habitID},
      "properties":{         "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "mention",
              "mention": {
                "type": "date",
                "date": { "start": habit_tracker_title, "end": None }
              },
              "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default"
              },
              "plain_text": habit_tracker_title,
              "href": None
            },
            {
              "type": "text",
              "text": { "content": " ", "link": None },
              "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default"
              },
              "plain_text": " ",
              "href": None
            }
          ]
        },
        "Daily Journal": {
          "id": "SWoy",
          "type": "relation",
          "relation": [{ "id": journal_id_created }]
        },
                  }
               }

  data = json.dumps(newEntryData)
  response = requests.request("POST",pageURL,headers=headers,data=data)
  return response