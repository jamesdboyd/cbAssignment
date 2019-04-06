import os.path
import logging
from logging import handlers

## Default log file name.
LOG_FILE="log/default.log"
## Before using qlog.log.info() or any of the other methods (debug, warning, error or critical)
## the mehod initialize must be called to initialized the Logger
flog = None ## File logger
clog = None ## Console logger
formatting = None ## Logging formatting
debug = False

def initialize( name=LOG_FILE ):
   ''' 
   This method must be called before using the log facility 
   param name: The name of the log file to use.
   '''
   global LOG_FILE
   global flog
   global clog
   global formatting
   global debug
   if(flog is None):
      if(name is None):
         name = LOG_FILE
      if(formatting is None):
         formatting = logging.Formatter("%(asctime)s %(levelname)s (%(filename)s:%(lineno)s) %(message)s")

      ## Check if log file exists.
      if(not os.path.exists(name)):
         dirs=os.path.dirname(name)
         if(not os.path.exists(dirs)):
            os.makedirs(dirs)
         os.open(name, os.O_CREAT)

      maxFileSize = 1024*1024*5 ## Bytes
      flog = logging.getLogger('awsFileLogger')
      rfh = handlers.RotatingFileHandler(filename=name, maxBytes=maxFileSize, backupCount=2)
      ## myLog = logging.getLogger("awsLogger")
      rfh.setFormatter(formatting)
      flog.addHandler(rfh)
      flog.setLevel(logging.DEBUG)
      flog.info("Initialized file logging")

   if(clog is None):
      clog = logging.getLogger('awsConsoleLogger')
      sh = logging.StreamHandler()
      sh.setFormatter(formatting)
      clog.addHandler(sh)
      clog.setLevel(logging.DEBUG)
      ##clog.info("Initialize Console Logging")


def main():
   initialize()
   clog.info("INFO This is the console logger .....")
   flog.debug("DEBUG message .....")
   flog.info("INFO This is the file logger ("+LOG_FILE+") .....")
   flog.warning("WARNING message .....")
   flog.error("ERROR message .....")
   flog.critical("CRITICAL message .....")

if __name__ == "__main__":
   main()
