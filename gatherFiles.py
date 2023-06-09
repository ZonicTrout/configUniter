import os
import json
import libFiles

libFiles.checkOS()

if "configFiles" not in libFiles.inWorkDir:
    os.mkdir( f'{libFiles.pwd}/configFiles' )
    
if "backupDir" not in libFiles.inWorkDir:
    os.mkdir( f'{libFiles.pwd}/backupDir' )

newConfigFolder = f'{libFiles.pwd}/configFiles'

configDict = {}

for configFilePath in libFiles.filesList:
    fileName = configFilePath.split("/")[-1]
    command = f'cp {configFilePath} {newConfigFolder}'
    configDict.update( {configFilePath: fileName} )
    os.system( command )
    
libFiles.BackUp(newBackupDir="configFiles")


