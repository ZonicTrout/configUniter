import os
import json
import libFiles

if os.name == "nt":
    print("Do not run this on Windows, bozo")
    exit()

homePath = os.path.expanduser('~')
pwd = os.getcwd()
inWorkDir = os.listdir(pwd)
configDir = f'{pwd}/configFiles'

if "fileMap.json" not in inWorkDir:
    print( "Do you have a filemap json file?" )
    exit()

with open("fileMap.json", "r") as jsonMap:
    global fileMap
    fileMap = json.load(jsonMap)

for path, fileName in fileMap.items():
    command = f'cp {configDir}/{fileName} {path}'
    print(command)