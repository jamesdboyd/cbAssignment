'''
Created on Apr 5, 2019

@author: jboyd
'''
import unittest
from services import utilities
from logger import cblog
from exception import exceptions

class TestUtilities(unittest.TestCase):

   def __INIT__(self, *args, **kwargs):
      super(TestUtilities, self).__INIT__(*args, **kwargs)

   def setUp(self):
      cblog.initialize()

   def tearDown(self):
      pass
   
   def test_uniqueList(self):
      util = utilities.Utilities()
      ## Test the utility works
      s = "6,2,3,4,5,6,3,3,2"
      valid = [4, 5]
      res = util.uniqueList(s)
      self.assertEqual(valid.sort(), res.sort())

      ## Validate large numbers work
      s = "1234567890123456789, 234567890123456789444522167345555, 1234567890123456789"
      valid = [234567890123456789444522167345555]
      res = util.uniqueList(s)
      self.assertEqual(valid.sort(), res.sort())

      ## Validate negative numbers
      s = "-2,5,1,-2,-3"
      valid = [5,1,-3]
      res = util.uniqueList(s)
      self.assertEqual(valid.sort(), res.sort())

      ## Test for invalid characters
      s = "1,2,A,3,2,%"
      with self.assertRaises(exceptions.CBInvalidDataException) as context:
         util.uniqueList(s)
      self.assertTrue(str(context.exception)) ## Check we got an exception
      
      ## Validate we handle spaces
      s = "33, 4 , 22   , 33 , 4    ,3"
      valid = [3, 22]
      res = util.uniqueList(s)
      self.assertEqual(valid.sort(), res.sort())
      
      ## Validate empty list
      s = "1,1,1,1,1,1,1,1"
      valid = []
      res = util.uniqueList(s)
      self.assertEqual(valid.sort(), res.sort())
