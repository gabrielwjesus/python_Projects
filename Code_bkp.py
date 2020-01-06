#This archive call for the type of backup and create log.
#By Gabriel Wilhelm de Jesus

import time

date =  time.strftime("%Y-%m-%d")

def createBkpFull():
        bkpfile = '%s-bkp-full.tar.gz' % date
        login_user = "USER"
        server = "SERVER"
        pathTo = '/mnt/bkp/%s' % bkpfile
        pathFrom = 'PATH FROM'
        exclude = '*.log, *.temp, .recycle'
        opts = 'Cravzp'
        bkp = 'rsync -%s %s@%s:%s %s' %(opts,login_user,server,pathFrom,pathTo)

        return bkp

def createLog():
        logFile = '%s-bkp-full.txt' % date
        pathLog = '/var/log/backup-full/%s' % logFile

        return pathLog

