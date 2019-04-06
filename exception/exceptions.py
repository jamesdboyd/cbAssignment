'''
Created on Apr 4, 2019

@author: jboyd
'''

class CBFileNotFoundException(Exception):
   def __init__(self, message=""):
      self.message = message
      
   def getMessage(self):
      return self.message

class CBFileExistsException(Exception):
   def __init__(self, message=""):
      self.message = message
      
   def getMessage(self):
      return self.message
   
class CBInvalidDataException(Exception):
   def __init__(self, message=""):
      self.message = message
      
   def getMessage(self):
      return self.message
