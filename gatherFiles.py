import os
import json

if os.name == "nt":
    print("Do not run this on Windows, bozo")
    exit()

homePath = os.path.expanduser('~')
pwd = os.getcwd()
inWorkDir = os.listdir(pwd)

Xresource = f'{homePath}/.Xresources'
i3Config = f'{homePath}/.config/i3/config'
filesList = [i3Config, Xresource]


if "configFiles" not in inWorkDir:
    os.mkdir( f'{pwd}/configFiles' )

newConfigFolder = f'{pwd}/configFiles'

configDict = {}

for configFilePath in filesList:
    fileName = configFilePath.split("/")[-1]
    command = f'cp {configFilePath} {newConfigFolder}'
    configDict.update( {configFilePath: fileName} )
    os.system( command )
    

for key, item in configDict.items():
    print (key + "\t" + item)

configJson = json.dumps(configDict, indent=4)

with open( f'{pwd}/fileMap.json', "w" ) as configFile:
    configFile.write(configJson)

