#!/usr/bin/python3
from argparse import RawTextHelpFormatter
import argparse
from logger import cblog
from services import locations
from services import utilities

args = None
def main():

   ## command line arguments
   cliArgs = argparse.ArgumentParser(description="Carbon Black Assessment Test", formatter_class=RawTextHelpFormatter)
   
   """
   ss = "Copy File: "
   ss += "where IN is the input file and OUT is the output file."
   cliArgs.add_argument('-b', '--copy-file', dest='copyFile', nargs=2, metavar=('IN', 'OUT'), type=str, help=ss)
   """

   ss = "Enable debug"
   cliArgs.add_argument('-d', '--debug', action='store_const', const="debug", help=ss)

   ss = "Get Carbon Black locations: "
   ss += "where OUT-FILE is the output file containing the locations"
   cliArgs.add_argument('-w', '--get-locations', dest='createLocationsFile', nargs=1, metavar=('OUT-FILE'), type=str, help=ss)

   ss = "Get unique list: "
   ss += "where LIST is the comma separated list to check. Returns to console unique list."
   cliArgs.add_argument('-u', '--unique-list', dest='getUniqueList', nargs=1, metavar=('LIST'), type=str, help=ss)

   global args
   args = cliArgs.parse_args()
   
   ## initialize logging
   cblog.initialize()
      
   if args.debug is not None:
      cblog.debug = True
      
   try:
      if args.createLocationsFile is not None:
         file = args.createLocationsFile[0]
         loc = locations.Locations(file)
         loc.getLocations()
      elif args.getUniqueList is not None:
         util = utilities.Utilities()
         res = util.uniqueList(args.getUniqueList[0])
         res.sort()
         print(res)
         """
      elif args.copyFile is not None:
         util = utilities.Utilities()
         util.copyFile(args.copyFile[0], args.copyFile[1] )
         """
      else:
         print("You did not specify anything to do!")
   except RuntimeError:
      pass
      
if __name__ == "__main__":
   main()
