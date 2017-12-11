import dropbox
import os
import glob
import re, fnmatch

dbx = dropbox.Dropbox(<<FILL IN THE ACCESS TOKEN HERE>>)

wd = ''

display = '/'
cmd = raw_input(display+'$ ');

while (cmd != "exit"):
	cmd = cmd.split(" ")
	if (cmd[0]=='ls'):
		for entry in dbx.files_list_folder(wd).entries:
			print(entry.name)
	if (cmd[0]=='cd'):
		if (cmd[1] == '..'):
			if(wd != ''):
				wd = os.path.dirname(wd);
				display = wd;
				if (wd == '/'):
					wd = '';
		else: 
			wd = wd + '/'+cmd[1];
			display = wd
	if (cmd[0]=='get'):
		fnam = wd+'/'+cmd[1]
		dbx.files_download_to_file(os.path.abspath(cmd[1]), fnam);
	if (cmd[0]=='mkdir'):
		dbx.files_create_folder(wd+"/"+cmd[1])
	if (cmd[0]=='put'):
		with open(cmd[1]) as f:
			dbx.files_upload(f.read(), wd+"/"+cmd[1], mute = True)
	if (cmd[0]=='mput'):
		for filename in glob.glob(cmd[1]):
			with open(filename) as f:
				dbx.files_upload(f.read(), wd+"/"+filename, mute = True)
	if (cmd[0]=='mget'):
		regexp = fnmatch.translate(cmd[1])
		reobj = re.compile(regexp);
		for entry in dbx.files_list_folder(wd).entries:
			if (reobj.match(entry.name)):
				fnam = wd+'/'+entry.name
				print entry.name
				dbx.files_download_to_file(os.path.abspath(entry.name), fnam);
				
			
			
		
			

	cmd = raw_input(display+'$ ');


