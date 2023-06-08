import os

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
    command = f'cp {configFilePath} {newConfigFolder}'
    configDict.update( {configFilePath: configFilePath.split("/")[-1]} )
    os.system( command )
    

for key, item in configDict.items():
    print (key + "\t" + item)

