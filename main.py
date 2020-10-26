import os
import os.path
plugins = os.listdir("Plugins")
for plugin in plugins:
    if (plugin.lower().endswith('.py')):
        exec("from Plugins." + plugin.replace(".py", "") + " import *")
        if(plugin=='Plugin.py'):
          import os
          os.rename('Plugins/Plugin.py','Plugins/'+pluginName+'.py')
        print(pluginName + ' Imported')


def pyloader(url):
  try:
      from urllib.request import urlretrieve as downloadFile
      b = url.split(' ')
      if(b[-1] == 'url'):
        downloadFile(b[0], 'Plugins/Plugin.py')
        print('Successfully downloaded plugin from url')
        print('Use the reboot command to install plugins completly')
      elif(b[-0]==' '):
        print('pyloader - downloads plugins via url or name on portal')
        print('if you would to download from a url please put "pyloader url [URL]"')
      else:
        downloadFile('https://pyshell-plugin-portal.errortp.repl.co/Plugins/'+ b[-1] + '.py','Plugins/Plugin.py')
        print('Successfully downloaded plugin from the portal')
        print('Use the reboot command to install plugins completly')
  except Exception as error:
    print('This is a invalid plugin if you were meaning to install from url')
    print('Please type "pyloader url [URL]" otherwise please try to find')
    print('The plugin you specified on https://pyshell-plugin-portal.errortp.repl.co/ and copy the link of said plugin')
    print(error)


def reboot(a):
  import sys
  if(sys.platform == 'linux'):
      os.system('clear')
      python = sys.executable
      os.execl(python, python, * sys.argv)
  elif(sys.platform == 'win32' or 'win64'):
      os.system('cls')
      python = sys.executable
      os.execl(python, python, * sys.argv)
  elif(sys.platform == 'OS X'):
      os.system('printf \33c\e[3J')
      python = sys.executable
      os.execl(python, python, * sys.argv)
  else:
    python = sys.executable
    os.execl(python, python, * sys.argv)

def help(args):
  def parseFile(file):
      with open(file) as f:
          linesList = f.read().splitlines()
          functions = []
      for line in linesList:
          if line.lower().startswith("def"):
              functions.append(line.split("def ")[1].split("(")[0])
      return functions

  print("Defined functions in", args)

  parsedFunctions = None
  if os.path.exists(args + ".py"):
      parsedFunctions = parseFile(args + ".py")
  if os.path.exists("Plugins/" + args + ".py"):
      parsedFunctions = parseFile("Plugins/" + args + ".py")

  if args.lower() == "help":
      parsedFunctions = parseFile("main.py")
  elif not parsedFunctions:
      print("No plugin or main function called:",args)
      return
  
  num = 0
  string = "\t"
  for func in parsedFunctions:
    if num > 4:
      print(string)
      num = 0
      string = "\t"
    string += func + "   "
    num += 1
  print(string)


def time(a):
    import datetime
    currenttime = str(datetime.datetime.now())
    print(currenttime)


def oscommand(runcommand):
    import time
    oscommand = runcommand
    if oscommand in ['rm', 'touch', 'cut', 'chmod', 'chgrp', 'cat', 'sudo']:
        print('You do not have permission to run this command')
    else:
        print(' ')
        print('Output:')
        print(' ')
        os.system(oscommand)
        print(' ')
        time.sleep(0.5)


def spam(text):
    while (True):
        print(text)


def echo(text):
    print(text)
    print(' ')

bootup = True
if(bootup == True):
  version = '1.0.0'
  print(version)
  import sys
  print('Pyshell on ' + sys.platform)
  print('help for a list of commands')
  bootup = False

while (True):
    command = input("Shell > ")
    commandSplit = command.split(" ", 1)
    lowercommand = commandSplit[0].lower()
    commandvar = commandSplit[-1]
    hsplit = command.split(" ", 1)
    try:
      if hsplit[0].lower() == "help":
        help(hsplit[-1])
      else:
          eval(lowercommand + "('" + commandvar + "')")
    except NameError:
        print("Unknown command [ " + command + " ]")
    except Exception as error:
        print(str(error))
        print(' ')
        print('An error occured, Please check if this is a valid command')
