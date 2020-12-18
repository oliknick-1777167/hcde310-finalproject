import urllib.parse, urllib.request, urllib.error, json
from flask import Flask, render_template, request

app = Flask(__name__)

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

baseurlPlayers = 'https://www.balldontlie.io/api/v1/players'
baseurlStats = 'https://www.balldontlie.io/api/v1/season_averages'
baseurlSearch = "https://www.balldontlie.io/api/v1/players"

def getPlayerAttributes(id):
    statsRequest = baseurlPlayers + "/" + str(id)
    x = urllib.request.urlopen(statsRequest)
    statsRequeststr = x.read()
    attributes = json.loads(statsRequeststr)
    return (attributes)

def getPlayerid(search):
    statsRequest = baseurlSearch + "?search=" + str(search)
    x = urllib.request.urlopen(statsRequest)
    statsRequeststr = x.read()
    attributes = json.loads(statsRequeststr)
    data = attributes['data']
    ids = []
    for i in range(len(data)):
        id = data[i]['id']
        ids.append(id)
    return (ids)


def getPlayerStats(season,player_ids):
    params = {}
    params['season'] = season
    params['player_ids[]'] = player_ids

    statsRequest = baseurlStats + "?" + urllib.parse.urlencode(params)

    x = urllib.request.urlopen(statsRequest)
    statsRequeststr = x.read()
    stats = json.loads(statsRequeststr)
    return (stats)

@app.route("/")
def main_handler():
    return render_template('greetform.html',page_title="Greeting Form")

def comparePlayerSeason(player_ids, season1 = 2019, season2=2018):
    season1 = season1
    season2 = season2
    statshtml = "<!DOCTYPE html><html><head><title>NBA Statistics</title></head><body style='background-color:#DBF3FA'>"
    statshtml += "<style>.header{color:blue; background: #DBF3FA; text-align: center; padding: 30px}</style>"

    for i in range(len(player_ids)):
        player = player_ids[i]
        results1 = getPlayerStats(season1,player)
        statstest1 = results1['data']

        results2 = getPlayerStats(season2, player)
        statstest2 = results2['data']

        if statstest1 and statstest2:
            stats1 = results1['data'][0]
            points1 = stats1.get('pts')
            assists1 = stats1.get('ast')
            fgMade1 = stats1.get('fgm')
            fgAttempt1 = stats1.get('fga')
            if fgAttempt1 != 0:
                fgPercent1 = (fgMade1 / fgAttempt1)
            else:
                fgPercent1 = 0.0
            fgPercent1 = round(fgPercent1, 2) * 100
            threesMade1 = stats1.get('fg3m')
            threesAttempt1 = stats1.get('fg3a')
            if threesAttempt1 != 0:
                threePercent1 = (threesMade1 / threesAttempt1)
            else:
                threePercent1 = 0.0
            threePercent1 = round(threePercent1, 2) * 100
            games1 = stats1.get('games_played')
            rebounds1 = stats1.get('reb')

            stats2 = results2['data'][0]
            points2 = stats2.get('pts')
            assists2 = stats2.get('ast')
            fgMade2 = stats2.get('fgm')
            fgAttempt2 = stats2.get('fga')
            if fgAttempt2 != 0:
                fgPercent2 = (fgMade2 / fgAttempt2)
            else:
                fgPercent2 = 0.0
            fgPercent2 = round(fgPercent2, 2) * 100
            threesMade2 = stats2.get('fg3m')
            threesAttempt2 = stats2.get('fg3a')
            if threesAttempt2 != 0:
                threePercent2 = (threesMade2 / threesAttempt2)
            else:
                threePercent2 = 0.0
            threePercent2 = round(threePercent2, 2) * 100
            games2 = stats2.get('games_played')
            rebounds2 = stats2.get('reb')
        elif statstest1 and not statstest2:
            stats1 = results1['data'][0]
            points1 = stats1.get('pts')
            assists1 = stats1.get('ast')
            fgMade1 = stats1.get('fgm')
            fgAttempt1 = stats1.get('fga')
            if fgAttempt1 != 0:
                fgPercent1 = (fgMade1 / fgAttempt1)
            else:
                fgPercent1 = 0.0
            fgPercent1 = round(fgPercent1, 2) * 100
            threesMade1 = stats1.get('fg3m')
            threesAttempt1 = stats1.get('fg3a')
            if threesAttempt1 != 0:
                threePercent1 = (threesMade1 / threesAttempt1)
            else:
                threePercent1 = 0.0
            threePercent1 = round(threePercent1, 2) * 100
            games1 = stats1.get('games_played')
            rebounds1 = stats1.get('reb')

            points2 = 'None'
            assists2 = 'None'
            fgMade2 = 'None'
            fgAttempt2 = 'None'
            fgPercent2 = 'None'
            threesMade2 = 'None'
            threesAttempt2 = 'None'
            threePercent2 = 'None'
            threePercent2 = 'None'
            games2 = 'None'
            rebounds2 = 'None'
        elif statstest2 and not statstest1:
            points1 = 'None'
            assists1 = 'None'
            fgMade1 = 'None'
            fgAttempt1 = 'None'
            fgPercent1 = 'None'
            threesMade1 = 'None'
            threesAttempt1 = 'None'
            threePercent1 = 'None'
            threePercent1 = 'None'
            games1 = 'None'
            rebounds1 = 'None'

            stats2 = results2['data'][0]
            points2 = stats2.get('pts')
            assists2 = stats2.get('ast')
            fgMade2 = stats2.get('fgm')
            fgAttempt2 = stats2.get('fga')
            if fgAttempt2 != 0:
                fgPercent2 = (fgMade2 / fgAttempt2)
            else:
                fgPercent2 = 0.0
            fgPercent2 = round(fgPercent2, 2) * 100
            threesMade2 = stats2.get('fg3m')
            threesAttempt2 = stats2.get('fg3a')
            if threesAttempt2 != 0:
                threePercent2 = (threesMade2 / threesAttempt2)
            else:
                threePercent2 = 0.0
            threePercent2 = round(threePercent2, 2) * 100
            games2 = stats2.get('games_played')
            rebounds2 = stats2.get('reb')
        else:
  
            #return render_template('nameerror.html',name = 'This player')
            continue

        # points1 = stats1.get('pts')
        # assists1 = stats1.get('ast')
        # fgMade1 = stats1.get('fgm')
        # fgAttempt1 = stats1.get('fga')
        # if fgAttempt1 != 0:
        #     fgPercent1 = (fgMade1 / fgAttempt1)
        # else:
        #     fgPercent1 = 0.0
        # fgPercent1 = round(fgPercent1,2) * 100
        # threesMade1 = stats1.get('fg3m')
        # threesAttempt1 = stats1.get('fg3a')
        # if threesAttempt1 != 0:
        #     threePercent1 = (threesMade1 / threesAttempt1)
        # else:
        #     threePercent1 = 0.0
        # threePercent1 = round(threePercent1, 2) * 100
        # games1 = stats1.get('games_played')
        # rebounds1 = stats1.get('reb')
        # else:
        #     points1 = 'None'
        #     assists1 = 'None'
        #     fgMade1 = 'None'
        #     fgAttempt1 = 'None'
        #     fgPercent1 = 'None'
        #     threesMade1 = 'None'
        #     threesAttempt1 = 'None'
        #     threePercent1 = 'None'
        #     threePercent1 = 'None'
        #     games1 = 'None'
        #     rebounds1 = 'None'


        # if statstest2:
        #     stats2 = results2['data'][0]
        # else:
        #     continue

        # points2 = stats2.get('pts')
        # assists2 = stats2.get('ast')
        # fgMade2 = stats2.get('fgm')
        # fgAttempt2 = stats2.get('fga')
        # if fgAttempt2 != 0:
        #     fgPercent2 = (fgMade2 / fgAttempt2)
        # else:
        #     fgPercent2 = 0.0
        # fgPercent2 = round(fgPercent2,2) *100
        # threesMade2 = stats2.get('fg3m')
        # threesAttempt2 = stats2.get('fg3a')
        # if threesAttempt2 != 0:
        #     threePercent2 = (threesMade2 / threesAttempt2)
        # else:
        #     threePercent2 = 0.0
        # threePercent2 = round(threePercent2,2) * 100
        # games2 = stats2.get('games_played')
        # rebounds2 = stats2.get('reb')

        results = getPlayerAttributes(player)

        firstname = results['first_name']
        lastname = results['last_name']
        statshtml += "<header class = 'header'>Here are the season averages for {} {}<header>".format(firstname,lastname)
        statshtml += render_template('statsTable.html',season = season1,gp=games1,points = points1, assists = assists1,rebounds = rebounds1, fgpercent = fgPercent1, threesMade = threesMade1,threePercent = threePercent1,season2 = season2,gp2=games2,points2 = points2, assists2 = assists2,rebounds2 = rebounds2, fgpercent2 = fgPercent2, threesMade2 = threesMade2,threePercent2 = threePercent2)
    statshtml += "</body></html>"
    return statshtml


def comparePlayerSeason_Safe(player_ids, season1 = 2019, season2 =2018 ):
    try:
        return comparePlayerSeason(player_ids,season1,season2)
    except urllib.error.URLError as m:
        if hasattr(m, 'code'):
            return ("Error trying to retrieve data: " + str(m))
        elif hasattr(m, 'reason'):
            return("We failed to reach a server")
            return("Reason: ", m.reason)
        return None

@app.route('/gresponse')
def player_stats_handler():
    name = request.args.get('username')
    season1 = request.args.get('season1')
    season2 = request.args.get('season2')
    #result = '<!DOCTYPE html><html><head><title>Name Response</title><header style="text-align: center; padding: 60px;font-size: 20px">Which Player Did you mean?</header></head><body style="background-color: #4aa3df; padding: 60px;font-size: 16px">"<form action="gresponse" method="get" style="text-align: center">'
    if name:
        id = getPlayerid(name)
        ids = []
        ids += id
        if ids:
            # result = render_template('nameResponse.html',ids = ids)
            # for player in ids:
            #     results = getPlayerAttributes(player)
            #     firstname = results['first_name']
            #     lastname = results['last_name']
            #     fullname = firstname + " " + lastname
            #     result += '<input type="checkbox" name="greet_type" value="hello" id="hello"/><label for="hello">({}) {}</label><br />'.format(player,fullname)
            result = comparePlayerSeason_Safe(ids,season1 = season1,season2=season2)
            # result += "<input type='submit' value='Go' name='gobtn'/> </form><div class= 'formtitle'></div></body></html>"
            return result
        else:
            return render_template('nameerror.html',name = name)




if __name__ == "__main__":
    # Used when running locally only.
	# When deploying to Google AppEngine, a webserver process
	# will serve your app.
    app.run(host="localhost", port=8080, debug=True)


ids = [237,115,250]
#getPlayerAttributes(237)
#getPlayerStats(2018,237)
#comparePlayerSeason_Safe(2016,2019,ids)
#comparePlayerSeason(2016,2019,ids)