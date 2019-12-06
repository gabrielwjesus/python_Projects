#This is de Main Backup PYTHON script
#we are going to backup FILES from a FileServer in another BackupServer
#Incremental Backup is not ready yet
#Created by Gabriel Wilhelm de Jesus November 2019.

import Code_bkp
import time
import subprocess

LOG = Code_bkp.createLog()
BKP = Code_bkp.createBkpFull()
BKPi = Code_bkp.createBkpInc()

def registerLog(startTime, BKP, LOG):
        date = (time.strftime('%d-%m-%Y'))
        r = open(LOG,"w+")
        log_message = 'LOG REGISTER\nDATE: %s\nSTART TIME:%s\nBKP FILE: %s\n' % (date,startTime,BKP)
        r.write(log_message)
        r.close()

def full():
        disk = '/dev/sda6'
        startTime =  time.strftime("%H:%M:%S")
        log = ' >> %s' % LOG

        mount = 'mount -a'
       subprocess.call(mount, shell=True)

       subprocess.call(BKP + log, shell=True)

        registerLog(startTime, BKP, LOG)
full()
