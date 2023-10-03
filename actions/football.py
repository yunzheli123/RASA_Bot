import http.client
import json

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e5cab1dbc83bd9e3a4316f28626d3d0"
    }

league = 39
season = 2023

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

def winLossRecord(name):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    team = getTeamsID(name)
    endpoint = "/teams/statistics?season=%d&league=%d&team=%d" % (
        season, league, team)
    conn.request("GET", endpoint, headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    
    if result['response']['fixtures']['played']['total'] == 0:
        text_message = "They have not played any game in this season"
        return text_message
    
    text_message = "Their record is {} wins, {} loss and {} draws.".format(
        result['response']['fixtures']['wins']['total'],
        result['response']['fixtures']['loses']['total'],
        result['response']['fixtures']['draws']['total'],
    ) 
    
    return text_message
