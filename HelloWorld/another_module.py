from pathlib import Path


#Absolute path
#c:Program files\Desktop
#Relative path

path= Path()
for file in path.glob('*'):
    print(file)