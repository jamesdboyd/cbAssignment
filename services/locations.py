'''
Created on Apr 4, 2019

@author: jboyd
'''
import os.path
import requests
import re
from logger import cblog
from exception import exceptions

class Locations:
   def __init__(self, outfile):
      self.outfile = outfile
      self.uri = "https://lifeatcb.carbonblack.com/locations/"
      self.lst = []

   def getLocations(self):
      self.processRequest()
      return self.lst

   def getLocationsUri(self, uri):
      self.uri = uri
      self.processRequest()
      return self.lst
      
   def processRequest(self):
      if self.outfile.endswith("/"):
         s = "You must specify a valid filename"
         cblog.flog.error(s)
         raise(exceptions.CBInvalidDataException(s))

      response = requests.request("GET", self.uri)
      data = response.content.decode(); 
      for line in data.splitlines(): ## iterate over data, line by line
         ## Luckily there is a unique pattern we can use to find the locations
         m = re.search(".*\s+<h1\s+class=\"heading\">(.*)<\/h1><\/div>$", line)
         if m is not None:
            loc = m.group(1)
            tmp = loc.split()
            if len(tmp) < 3: ## One of the entries is not a location, it contains 4 strings
               if loc not in self.lst: ## We don't want duplicates
                  self.lst.append(loc)
                  if cblog.debug:
                     cblog.debug(loc)
      
      ## We don't want to overwrite an existing file
      if os.path.isfile(self.outfile):
         s = "The file "+self.outfile+" already exists."
         cblog.flog.error(s)
         raise exceptions.CBFileExistsException(s)

      d = self.getDirectory(self.outfile)
      if d is not None and not d == "":
         if not os.path.exists(d):
            os.makedirs(d)
      ## print(data);
      ## With data to file
      try:
         with open(self.outfile, "w", encoding='ISO-8859-1') as f:
            for l in self.lst:
               f.write(l+"\n")
      except FileNotFoundError:
         s = "The file or directory does not exist: "+self.outfile
         cblog.flog.error(s)
         raise exceptions.CBFileNotFoundException(s)
      
   def getDirectory(self, fileName):
      lst = fileName.split('/')
      directory = ""
      if len(lst) > 0:
         for d in lst[:-1]:
            directory += d+"/"
      return directory
         