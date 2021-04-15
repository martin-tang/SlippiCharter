from slippi import Game
import json
import os
print("Starting program...\n=====================================")
directory = './replay files/'
dict = {
    'slippiCount' : 0,
    'falcoGames' : 0,
    'foxGames' :0,
    'marthGames':  0 
}
for filename in os.listdir(directory):
    if filename.endswith(".slp"):
        dict['slippiCount'] += 1 
        if dict['slippiCount'] % 5 == 0:
            print(dict)
            #print("Slippi games processed: ", slippiCount, "falco: ", falcoGames, " fox: ",foxGames, " marth: ",marthGames)
        currGame = Game('replay files/'+filename)
        for i in currGame.metadata.players:
            if i is not None:
                if i.netplay.name == 'MoxieFoxy' or i.netplay.name=='DS4_Johns':
                    if 22 in i.characters.keys():
                        dict['falcoGames']+=1
                    if 1 in i.characters.keys():
                        dict['foxGames'] += 1
                    if 18 in i.characters.keys():
                        dict['marthGames'] += 1
        continue
    else:
        continue
print(dict)
print("=====================================\nExit successful!")