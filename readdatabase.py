import json, requests

def readDatabase(databaseURL,database_id,headers):
    readURL = databaseURL + database_id + '/query'
    query = {'filter': {"property":"title","text":{"contains":"Day"}}}
    response = requests.request("POST", readURL,headers=headers,data=query)
    databaseReadData = response.json()
    print(response.text)
    
    with open('./db.json','w',encoding='utf8') as f:
        json.dump(databaseReadData,f,ensure_ascii=False)