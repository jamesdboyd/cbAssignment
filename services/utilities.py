'''
Created on Apr 5, 2019

@author: jboyd
'''

import os;
import sys
from logger import cblog
from exception import exceptions

class Utilities:
   
   def __INIT__(self):
      pass
   
   """
   Find unique numbers in string of comma separated list of numbers
   """
   def uniqueList(self, searchString):
      result = []
      lst = searchString.split(",")
      ## check for valid data
      for i in lst:
         i.strip()
         if i.isalpha():
            s = "This is not a valid number"
            cblog.flog.error(s)
            raise(exceptions.CBInvalidDataException(s))
         
      hsh = {}
      for n in lst:
         if n not in hsh:
            hsh[n] = 1;
         else:
            c = hsh[n]
            hsh[n] = c + 1;
            
      for k, v in hsh.items():
         if( v == 1 ):
            result.append(int(k))
            
      return result
   
   """
   def copyFile(self, inName, outName):
      if not os.path.isfile(inName):
         s = "The input file does not exist"
         raise(exceptions.CBFileNotFoundException(s))
      
      gotException = False;
      ## Try opening file as text file
      with open(inName, "r") as f1:
         with open(outName, "w") as f2:
            data = f1.read(1)
            while( data ):
               try:
                  f2.write(data)
                  data = f1.read(1)
                  if data is None:
                     break
               except UnicodeDecodeError:
                  cblog.flog.error("Excp: "+str(sys.exc_info()[0]))
                  gotException = 1
                  break
                  
      ## Maybe this is a binary file, there must be a better solution to determine if a file is binary or test.
      if gotException == 1:
         with open(inName, "br") as f3:
            with open(outName, "bw") as f4:
               data = f3.read(1)
               while( data ):
                  f4.write(data)
                  data = f3.read(1)
                  if data is None:
                     break
   """