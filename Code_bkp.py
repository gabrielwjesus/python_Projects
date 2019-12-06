#This archive call for the type of backup and create log.
#By Gabriel Wilhelm de Jesus

import time

date =  time.strftime("%Y-%m-%d")

def createBkpFull():
        bkpfile = '%s-bkp-full.tar.gz' % date
        pathTo = '/mnt/bkp/%s' % bkpfile #destino
        pathFrom = 'bm-wilhelmdejesus@10.47.61.5:/DADOS/' #origem
        exclude = '*.log, *.temp, .recycle'
        opts = 'Cravzp'
        #bkp = 'rsync -%s --exclude={%s} %s %s' %(opts,exclude,pathFrom,pathTo)
        bkp = 'rsync -%s --rsh="ssh -l bm-wilhelmdejesus" --exclude={%s} %s %s' %(opts,exclude,pathFrom,pathTo)

        return bkp

def createBkpInc(): #not ready
        return True

def createLog():
        logFile = '%s-bkp-full.txt' % date
        pathLog = '/var/log/backup-full/%s' % logFile

        return pathLog
