'''
Created on Apr 4, 2019

@author: jboyd
'''
import os
import unittest
import tempfile
from services import locations
from logger import cblog
from exception import exceptions

class TestLocations(unittest.TestCase):
   
   def __INIT__(self, *args, **kwargs):
      super(TestLocations, self).__INIT__(*args, **kwargs)

   def setUp(self):
      cblog.initialize()
      self.outfile = "./cb-locations"
      if os.path.isfile(self.outfile):
         os.remove(self.outfile)

   def tearDown(self):
      self.outfile = "./cb-locations"
      if os.path.isfile(self.outfile):
         os.remove(self.outfile)
         
   """
   Test that the file is created and is not empty
   """
   def test_1(self):
      loc = locations.Locations(self.outfile)
      loc.getLocations()

      self.assertTrue(os.path.isfile(self.outfile), "The locations file "+self.outfile+" does not exist.")
      size = os.path.getsize(self.outfile)
      self.assertTrue(size > 0, "The locations file "+self.outfile+" is empty.")
      
   """
   Verify different output file names and different directories should work
   """
   def test_2(self):
      ofile = "FOO/BAR/1/2/3/cb-locations"
      loc = locations.Locations(ofile)
      loc.getLocations()
      self.assertTrue(os.path.isfile(ofile), "The file "+ofile+" was not created.")
      self.assertTrue(os.path.getsize(ofile) > 0, "The file is empty")
      os.remove(ofile)

      ## Test that non alpha/numeric characters are excepted
      ofile = "/tmp/1/%%%/#/*/^/cb-locations"
      loc = locations.Locations(ofile)
      loc.getLocations()
      self.assertTrue(os.path.isfile(ofile), "The file "+ofile+" was not created.")
      self.assertTrue(os.path.getsize(ofile) > 0, "The file is empty")
      os.remove(ofile)
      
   """
   Validate the locations file
   """
   def test_3(self):
      loc = locations.Locations(self.outfile)
      lst = loc.getLocations();
      res = []
      self.assertTrue(len(lst) > 0, "The list should not be empty")
      with open(self.outfile, "r") as f:
         for line in f.readlines():
            s = line.strip()
            res.append(s)
            
      self.assertTrue(lst == res, "The file list and method list should be the same.")
      
   """
   Verify we prevent the output file from overwriting an existing file
   """
   def test_4(self):
      tf, name = tempfile.mkstemp()
      loc = locations.Locations(name)
      with self.assertRaises(exceptions.CBFileExistsException) as context:
         loc.getLocations()
      self.assertTrue(str(context.exception)) ## Check we got an exception




