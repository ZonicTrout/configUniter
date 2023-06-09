import os
import json
from datetime import datetime



homePath = os.path.expanduser('~')
pwd = os.getcwd()
inWorkDir = os.listdir(pwd)

Xresource = f'{homePath}/.Xresources'
i3Config = f'{homePath}/.config/i3/config'
i3statusConfig = f'{homePath}/.config/i3status/config'
picomConfig = f'{homePath}/.config/picom/picom.conf'

filesList = [i3Config, Xresource, i3statusConfig, picomConfig]

backupDir = f'BackupDir'


def checkOS() -> None:
    if os.name == "nt":
        print("Do not run this on Windows, bozo")
        exit()
        
def BackUp( toBeSaved:list=filesList, newBackupDir=backupDir ):
    for oldFilePath in toBeSaved:
        currentDate:str = datetime.now()
        
        oldFileName = oldFilePath.split("/") [-1]
        newFileName = oldFilePath.replace("/", "_")
        
        cpCommand = f'cp {oldFilePath} "{pwd}/{newBackupDir}"'
        renCommand = f'mv {newBackupDir}/{oldFileName} {newBackupDir}/{newFileName}'

        command = f'{cpCommand} && {renCommand}'
        os.system(command)
        

