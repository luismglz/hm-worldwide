from random import randint
from django.db import models
from msilib.schema import Class

def generateID():
  letters = 'XX'
  value = randint(1000, 9999)
  return 'XX'+value
