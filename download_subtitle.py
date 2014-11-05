import basic_functions as bf
import os

CODECS = ["mp4", "avi", "mkv"]
EXP_LIST_FILE = os.path.join(os.getcwd(), "exp_list.txt")
SUBS_DOWNLOADED = os.path.join(os.getcwd(), "subsdownload.txt")
LANGUAGE = "en"

def download_subtitles_main():
  config_file_status = bf.file_exists(bf.CONFIG_FILE)
  if config_file_status:
    if bf.config_file_empty():
      return False
    else:
      dir_list = list_folders()
      files_without_subs = []
      for dir_name in dir_list:
        files_without_subs.append(video_files_list(dir_name))
      subs_download(files_without_subs)
      return True
  else:
    bf.initialize_config()
    return False

def subs_download(files_list_of_list):
  for folder in files_list_of_list:
    for file_name in folder:
      os.chdir(os.path.split(file_name)[0])
      status = os.system("subliminal -l %s -- %s" %(LANGUAGE, os.path.split(file_name)[-1]))
      if status != 0:
        fh = open(EXP_LIST_FILE,"a")
        fh.write("%s%s" %(file_name, "\n"))
        fh.close()
      else:
        fh = open(SUBS_DOWNLOADED, "a")
        fh.write("%s%s" %(file_name, "\n"))
        fh.close()
  return True

def list_folders():
  fh = open(bf.CONFIG_FILE)
  dir_list = fh.readlines()
  fh.close()
  dir_list = [x.rstrip("\n") for x in dir_list]
  return dir_list

def init_excep_list():
  fh = open(EXP_LIST_FILE,"w")
  fh.close()

def video_files_list(dir_name):
  video_files = []
  for (top, sub_folders, files) in os.walk(dir_name):
    for file_name in files:
      if file_name.split(".")[-1] in CODECS:
        video_files.append(os.path.abspath(os.path.join(top,file_name)))

  video_files = files_need_subtitle(video_files)
  video_files = files_notin_exception(video_files)
  return video_files


def files_need_subtitle(video_files):
  files_without_subs = []
  for file_path in video_files:
    (path, file_name) = os.path.split(file_path)
    file_without_ext = ".".join(file_name.split(".")[:-1])
    str_file = os.path.join(path, "%s.%s.%s" %(file_without_ext, LANGUAGE, "srt"))
    if not os.path.exists(str_file):
      files_without_subs.append(file_path)
  return files_without_subs

def files_notin_exception(files_list):
  if not os.path.exists(EXP_LIST_FILE):
    init_excep_list()
    return files_list
  else:
    fh = open(EXP_LIST_FILE)
    exp_files = fh.readlines()
    fh.close()
    exp_files = [x.strip("\n") for x in exp_files]
    files_exp_not = [file_token for file_token in files_list if file_token not in exp_files]
    return files_exp_not