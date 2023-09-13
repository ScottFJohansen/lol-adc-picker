
def addMatchup(matchup, status, matchupArray, champion):
    matchupArray[champion][status].append(matchup)
    return matchupArray

def createMatchupsArray(champions):
    matchupArray = {}
    for champion in champions:
        with open('data/matchups/' + champion.strip() + '.txt') as f:
            matchups = f.readlines()
        championObject = {}
        championObject['name'] = champion.strip()
        championObject['current'] = 0
        championObject['-'] = []
        championObject['+'] = []
        matchupArray[champion.strip()] = championObject
        status = ''
        for matchup in matchups:
            if matchup.strip() == '-':
                status = '-'
                continue
            elif matchup.strip() == '+':
                status = '+'
                continue
            matchupArray = addMatchup(matchup.strip(), status, matchupArray, champion.strip())
    return matchupArray

def getADCArray():
    championArray = []
    with open('data/adc.txt') as f:
        champions = f.readlines()
    for champion in champions:
        championArray.append(champion.strip())
    return championArray

def getMatchupsArray():
    with open('data/champions.txt') as f:
        champions = f.readlines()
    matchupArray = createMatchupsArray(champions)
    return matchupArray

def getChampionsArray():
    with open('data/allchampions.txt') as f:
        champions = f.readlines()
    championArray = []
    for champion in champions:
        championArray.append(champion.strip())
    return championArray
