import os
import json
import libFiles

if os.name == "nt":
    print("Do not run this on Windows, bozo")
    exit()

if "configFiles" not in libFiles.inWorkDir:
    os.mkdir( f'{libFiles.pwd}/configFiles' )

newConfigFolder = f'{libFiles.pwd}/configFiles'

configDict = {}

for configFilePath in libFiles.filesList:
    fileName = configFilePath.split("/")[-1]
    command = f'cp {configFilePath} {newConfigFolder}'
    configDict.update( {configFilePath: fileName} )
    os.system( command )
    

for key, item in configDict.items():
    print (key + "\t" + item)

configJson = json.dumps(configDict, indent=4)

with open( f'{libFiles.pwd}/fileMap.json', "w" ) as configFile:
    configFile.write(configJson)

