# OS Module 

import os
from datetime import datetime

print(os.getcwd())
os.chdir('/corejava/')
# print(os.getcwd())

# os.mkdir('tef.text')
#os.makedirs('os-demo')
# os.removedirs('os-demo')
# os.rename('tef.text','fay.text')
print(os.stat('fay.text'))
mod_time = os.stat('fay.text').st_mtime
print(datetime.fromtimestamp(mod_time))
# print(os.listdir())


#os.walk used to detail of all directories
for dirpath,dirnames,filenames in os.walk('/corejava/'):
    print('dir path: ',dirpath)
    print('dir names: ',dirnames)
    print('file names: ',filenames)
    print()
	

print(os.environ.get('HOME'))
file_path =os.path.join(os.environ.get('HOME'),'fst.text')
print(file_path)