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


backupDir = f'{pwd}/BackupDir'

def BackUp( toBeSaved:list, newBackupDir=backupDir ):
    for oldFilePath in toBeSaved:
        pass
        

