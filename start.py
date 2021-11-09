from slippi import Game
import json
import os

directory = './test files/'
dict = {
    'Games Played' : 0,
    'Falco Games' : 0,
    'Fox Games' :0,
    'Marth Games':  0 
}

def startmessage():
    print("starting script...")

def endmessage():
    print("exit successful!")

def chart():
    for filename in os.listdir(directory):
        if filename.endswith(".slp"):
            dict['slippiCount'] += 1 
        if dict['slippiCount'] % 5 == 0:
            print(dict)
        currGame = Game(directory+filename)
        'Game object is created here'
        for i in currGame.metadata.players:
            if i is not None:
                if i.netplay.name == 'FOXMASTER2000' or i.netplay.name=='DS4_Johns':
                    try: 
                        if 22 in i.characters.keys():
                            dict['falcoGames']+=1
                        if 1 in i.characters.keys():
                            dict['foxGames'] += 1
                        if 18 in i.characters.keys():
                            dict['marthGames'] += 1
                    except:
                        print("exception!")
            continue
        else:
            continue
    print(dict)

startmessage()
chart()
endmessage()
