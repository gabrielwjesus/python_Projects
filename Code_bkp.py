#This archive call for the type of backup and create log.
#By Gabriel Wilhelm de Jesus

import time

date =  time.strftime("%Y-%m-%d")
USER = your_user

def createBkpFull():
        bkpfile = '%s-bkp-full.tar.gz' % date
        pathTo = '/mnt/bkp/%s' % bkpfile
        pathFrom = 'USER@ADDRESS:PATH' #put your user address and path
        exclude = '*.log, *.temp, .recycle'
        opts = 'Cravzp'
        #bkp = 'rsync -%s --exclude={%s} %s %s' %(opts,exclude,pathFrom,pathTo)
        bkp = 'rsync -%s --exclude={%s} %s %s' %(opts,exclude,pathFrom,pathTo)

        return bkp

# def createBkpInc(): #not ready
#        return True

def createLog():
        logFile = '%s-bkp-full.txt' % date
        pathLog = '/var/log/backup-full/%s' % logFile

        return pathLog
