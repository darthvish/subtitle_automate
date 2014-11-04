
import sys
import os


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
    pass
  elif choice == 2:
    pass
  elif choice == 3:
    pass
  elif choice == 4:
    sys.exit(0)

def subliminal_exist_check():
  status = os.system("subliminal --version")
  if not status:
    return True
  else:
    return False