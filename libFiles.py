import os
import json
from datetime import datetime



homePath = os.path.expanduser('~')
pwd = os.getcwd()
inWorkDir = os.listdir(pwd)

Xresource = f'{homePath}/.Xresources'
i3Config = f'{homePath}/.config/i3/config'
filesList = [i3Config, Xresource]

backupDir = f'{pwd}/BackupDir'


def checkOS() -> None:
    if os.name == "nt":
        print("Do not run this on Windows, bozo")
        exit()
        
def BackUp( toBeSaved:list=filesList, newBackupDir=backupDir ):
    for oldFilePath in toBeSaved:
        currentDate:str = datetime.now()
        command = f'cp {oldFilePath} {oldFilePath}_copy{ currentDate }'
        os.system(command)
        

