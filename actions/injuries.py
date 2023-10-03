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

def getTeamFixture(name, date):
    # 读取网站内容
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    # conn.request("GET", "/injuries?fixture=686314", headers=headers)
    # conn.request("GET", "/fixtures?league=39&season=2023&date=2023-10-01&team=65", headers=headers)
    
    team = getTeamsID(name)
    endpoint = "/fixtures?league=%d&season=%d&date=%s&team=%d" % (
        league, season, date, team)
    conn.request("GET", endpoint, headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    
    try:
        fixture = result['response'][0]['fixture']['id']   
        return fixture
    
    except IndexError:
        return "e"

def getInjuries(name, date):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    # conn.request("GET", "/injuries?fixture=1035103", headers=headers)
    team = getTeamsID(name)
    fixture = getTeamFixture(name, date)
    
    if not isinstance(fixture, int):
        return fixture

    endpoint = "/injuries?fixture=%d" % (fixture)
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = json.loads(data)
    
    text_message_success = "Here is the injuries list: "
    for player_result in result['response']:
        if player_result['team']['id'] == team:
            text_message_success += "{} didn't take this match, the reason is {}. ".format(
                player_result['player']['name'],
                player_result['player']['type'],
            )
    return text_message_success
    
    
