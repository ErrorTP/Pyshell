import os
import os.path
plugins = os.listdir("Plugins")
for plugin in plugins:
    if(plugin.lower().endswith('.py')):
     exec("from Plugins." + plugin.replace(".py", "") + " import *")
     print(str(plugin) + ' Imported')

def conshelp(a):
    print(' ')
    print('Testshell commands')
    print('help - Shows help')
    print('exit - Exits')
    print('time - Shows the time of the server or if run locally your pc time')
    print(' ')

def time(a):
  import datetime
  currenttime = str(datetime.datetime.now())
  print(currenttime)

def oscommand(runcommand):
  import time
  oscommand = runcommand
  if oscommand in ['rm','touch','cut','chmod','chgrp','cat','sudo']:
    print('You do not have permission to run this command')
  else:
    print(' ')
    print('Output:')
    print(' ')
    os.system(oscommand)
    print(' ')
    time.sleep(0.5)

def spam(text):
  while(True):
    print(text)

def echo(text):
  print(text)
  print(' ')




version = '1.0.0'
print(version)
print('Pyshell')
print('help for a list of commands')

while(True):
  command = input("Shell > ")
  commandSplit = command.split(" ", 1)
  lowercommand = commandSplit[0].lower()
  commandvar = commandSplit[-1]
  try:
    if(command.lower()=='help'):
      conshelp('a')
    else:
          eval(lowercommand + "('" + commandvar + "')")
  except NameError:
    print("Unknown command [ " + command + " ]")
  except Exception as error:
    print(str(error))
    print(' ')
    print('An error occured, Please check if this is a valid command')
