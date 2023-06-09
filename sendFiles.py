import os
import libFiles

libFiles.checkOS()

os.chdir( f'{libFiles.pwd}/configFiles' )
print(os.getcwd())

os.system( "git init" )
os.system( "git branch -m main" )
os.system( "git add ." )
os.system( "git commit -m 'Updated dotFiles'" )
os.system( "git remote add origin https://github.com/ZonicTrout/rawConfigs.git" )
os.system( "git push origin main" )


command = f''