import csv
from functions import *



with open('shots_data.csv', 'r') as file:
    reader = csv.DictReader(file, skipinitialspace = True)




    teamBData = getTeamData('Team B', reader) 
    teamAData = getTeamData("Team A", reader)
    
    


    
    
    
                        
###### shots attempted in 2 pt zone
    def findTwoPercentage(data):
        totalShots = 0
        twoPointShots = 0
        for shot in data:
            totalShots += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) < 22:
                twoPointShots += 1
            elif hypotnuse(x, y) < 23.75 and y >= 7.8:
                twoPointShots += 1
        if totalShots == 0:
            return 0
        return twoPointShots / totalShots

########## shots attempted in NC3 zone

    def findNC3Percentage(data):
        ########## shots attempted in NC3 zone
        totalShots = 0
        twoPointShots = 0
        for shot in data:
            totalShots += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) > 23.75 and y >= 7.8:
                twoPointShots += 1
        if totalShots == 0:
            return 0
        return twoPointShots / totalShots




    def findC3Percentage(data):
        # finds the percentage of the shots that were attempted in the C3 zone
        totalShots = 0
        twoPointShots = 0
        for shot in data:
            totalShots += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) > 22 and y <= 7.8:
                twoPointShots += 1
        if totalShots == 0:
            return 0
        return twoPointShots / totalShots





 
    
    def twoPointfgmfga(data):
        #returns the field goals made and attempted in two point area
        shotsMade = 0
        total = 0
        for shot in data:
            total += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) < 22 and shot['fgmade'] == '1':
                shotsMade += 1
            elif hypotnuse(x, y) < 23.75 and y >= 7.8 and shot['fgmade'] == '1':
                shotsMade += 1
        return shotsMade , total



    def threePointfgmfga(data):
        #returns the field goals made and attempted in three point area
        shotsMade = 0
        total = 0
        for shot in data:
            total += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) > 23.75 and shot['fgmade'] == '1':
                shotsMade += 1
            elif hypotnuse(x, y) > 22 and y <= 7.8 and shot['fgmade'] == '1':
                shotsMade += 1
        return shotsMade , total

    def nc3fgmfga(data):
        #returns the fgm and fga in non-corner 3 zone given a teams data
        shotsMade = 0
        total = 0
        for shot in data:
            total += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) > 23.75 and y >= 7.8 and shot['fgmade'] == '1':
                shotsMade += 1
        return shotsMade , total

    def c3fgmfga(data):
        #returns the fgm and fga in corner 3 zone given a teams data
        shotsMade = 0
        total = 0
        for shot in data:
            total += 1
            x = float(shot['x'])
            y = float(shot['y'])
            if hypotnuse(x, y) >= 22 and y <= 7.8 and shot['fgmade'] == '1':
                shotsMade += 1
        return shotsMade , total

        

    fgm, fga = c3fgmfga(teamBData)
    threeFgm, threefga = threePointfgmfga(teamBData)


    


        
    def efg(fgm, fga, threeFgm):
        #returns efg of a team
        total = fgm + (.5 * threeFgm)
        return total / fga



