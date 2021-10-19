import json

def getIdFromJson(response):
    response_values = response.json()
    journal_id = (response_values['id'])
    return journal_id
    