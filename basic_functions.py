import os
# ./config.txt
CONFIG_FILE = "./config.txt"

def add_folder(dir_name):
  config_status = file_exists(CONFIG_FILE)
  dir_status = dir_exists(dir_name)
  if config_status:
    if dir_status:
      fh = open(CONFIG_FILE, "a")
      fh.write("%s%s" %(dir_name, "\n"))
      fh.close()
      return True
    else:
      return False
  else:
    initialize_config()
    if dir_status:
      fh = open(CONFIG_FILE, "a")
      fh.write("%s%s", %(dir_name, "\n"))
      fh.close()
      return True
    else:
      return False


def initialize_config():
  fh = open(CONFIG_FILE, "w")
  fh.close()


def file_exists(file_name):
  if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
    return True
  else:
    return False

def dir_exists(dir_name):
  if os.path.isdir(dir_name) and os.access(dir_name, os.R_OK):
    return True
  else:
    return False


def remove_folder():
  config_status = file_exists(CONFIG_FILE)
  if config_status:
    if config_file_empty():
      return False
    else:
      folders = folders_in_config()
  else:
    initialize_config()
    return False

def config_file_empty():
  fh = open(CONFIG_FILE, "r")
  text_lines = fh.readlines()
  fh.close()
  if text_lines <= 1:
    return True
  else:
    return False

def folders_in_config():
  fh = open(CONFIG_FILE, "r")
  files_lists = fh.readlines()
  fh.close()
  files_lists = [x.rstrip("\n") for x in files_lists]
  return files_lists