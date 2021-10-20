import json, requests

def readDatabase(databaseURL,database_id,headers):
    readURL = databaseURL + database_id + '/query'
    response = requests.request("POST", readURL,headers=headers)
    databaseReadData = response.json()
    print(response.status_code)
    
    with open('./db.json','w',encoding='utf8') as f:
        json.dump(databaseReadData,f,ensure_ascii=False)