from __future__ import unicode_literals
from babelfish import Language
#from datetime import timedelta
import subliminal
import basic_functions as bf


def download_subtitles_subliminal(subs_dirs):
    subliminal.cache_region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
    videos = subliminal.scan_videos(subs_dirs, subtitles=True)
    result = subliminal.download_best_subtitles(videos, {Language('eng')})
    return result


def download_subtitles_main():
    config_status = bf.file_exists(bf.CONFIG_FILE)
    if config_status:
        if bf.config_file_empty():
            return False
        else:
            subs_dirs = list_folders()
            download_subtitles_subliminal(subs_dirs)
            return True
    else:
        bf.initialize_config()
        return False


def list_folders():
    """
    >>> list_folders()
    ['/home/vish/testing', '/home/vish/Podcasts/Arrow', '/home/vish/Podcasts']
    """
    fh = open(bf.CONFIG_FILE)
    dir_list = fh.readlines()
    fh.close()
    dir_list = [x.rstrip("\n") for x in dir_list]
    return dir_list