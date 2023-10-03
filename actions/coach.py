import http.client
import json

season = 2023
league = 39

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e5cab1dbc83bd9e3a4316f28626d3d0"
    }

def getTeamsID(name):
    # 读取网站内容
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    endpoint = "/teams?season=%d&league=%d" % (
        season, league)
    conn.request("GET", endpoint, headers=headers)
    
    res = conn.getresponse()
    data_res = res.read()
    data = json.loads(data_res)
    teams_info = data['response']
    teams_dict = dict()
    for team in teams_info:
        key = team['team']['name']
        value = team['team']['id']
        teams_dict[key] = value
    ID = teams_dict[name]
    
    return ID 

def getCoachRecord(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    team = getTeamsID(name)
    endpoint = "/coachs?team=%d" % (team)
    conn.request("GET", endpoint, headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    
    if result['response'][0]['name'] == 0:
        text_message = "I'm afraid this team doesn't have a coach! Damn."
        return text_message
    

    text_message = "Their coach is {}, the legend. He was born in {}, and his first name is {}. His hometown is {}".format(
        result['response'][0]['name'],
        result['response'][0]['birth']['date'],
        result['response'][0]['firstname'],
        result['response'][0]['birth']['place'],
    )
         
    return text_message
