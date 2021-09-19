import pandas as pd;

try:
  hello_world()
except:
  print "An exception was thrown!"
  print str(error)
  assert False, f"raised an exception"
