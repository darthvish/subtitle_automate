__author__ = "vishvendra singh"
__version__ = 0.1

import sys
import os
import urllib
import basic_functions as bf
import download_subtitle as ds


def main():
  VALID_INPUTS = [1, 2, 3, 4]

  print "1. add folder for watch"
  print "2. remove folder"
  print "3. start downloading"
  print "4. exit"
  try:
    choice = int(raw_input("input:"))
    if choice not in VALID_INPUTS:
      print "not valid input"
  except:
    print "not valid input"

  if choice == 1:
    folder_name = raw_input("path$")
    if bf.add_folder(folder_name):
      os.system("clear")
      print "status:", "dir added to list"
      main()
    else:
      os.system("clear")
      print "status:", "given path is not valid"
      main()
  elif choice == 2:
    os.system("clear")
    print "status:", "option not ready till now"
    main()
  elif choice == 3:
    print "wait...."
    if ds.download_subtitles_main():
      os.system("clear")
      print "status:","operation successfully completed"
      main()
    else:
      os.sytem("clear")
      print "status:", "operation failed"
      print "status:", "add folders to list"
      main()
  elif choice == 4:
    sys.exit(0)

def subliminal_exist_check():
  status = os.system("subliminal --version")
  if not status:
    return True
  else:
    return False

def internet_connectivity_check():
  try:
    fh = urllib.urlopen("http://www.google.com")
  except IOError:
    return False
  fh.close()
  return True

def start_check():
  if subliminal_exist_check():
    if internet_connectivity_check():
      return True
    else:
      print "internet connectivity problem"
      return False
  else:
    print "subliminal not installed"
    return False


if __name__ == "__main__":
  if start_check():
    main()
  else:
    print "restart again after resolving given problems"
    sys.exit(0)