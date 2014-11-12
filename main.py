__author__ = "vishvendra singh"
__version__ = 0.1

import sys
import os
import urllib
import basic_functions as bf
import download_subtitle as ds


def print_msg(msg):
    os.system("clear")
    print "msg: "+msg
    cli_menu()


def cli_menu():
    print "1. add folder to watch"
    print "2. remove folder"
    print "3. downloading subtitles"
    print "4. exit"
    choice = input("your choice: ")
    if user_choice_validate(choice):
        interpret_usr_choice(choice)
    else:
        print_msg("msg: choice not valid, possible values are 1, 2, 3, 4")


def user_choice_validate(value):
    if isinstance(value, int) and value in [1, 2, 3, 4]:
        return True
    else:
        return False


def interpret_usr_choice(choice):
    if choice == 1:
        cli_add_dir()
    elif choice == 2:
        print_msg("this option is not available till now")
    elif choice == 3:
        cli_dl_subs()
    elif choice == 4:
        sys.exit(0)


def cli_add_dir():
    dir_path = raw_input("input folder path:>>> ")
    if bf.add_folder(dir_path):
        print_msg("folder added successfully")
    else:
        print_msg("given folder not exist, check your input")


def cli_dl_subs():
    if ds.download_subtitles_main():
        print_msg("subs downloaded successfully")
    else:
        print_msg("add folders to list first")


def subliminal_exist_check():
    """
    check for installation of subliminal on user's computer
    >>> subliminal_exist_check()
    True

    :return:
    """
    try:
        import subliminal
    except ImportError:
        return False
    else:
        return True


def internet_connectivity_check():
    """
    checks for internet connectivity on user's computer
    >>> internet_connectivity_check()
    True

    :return:
    """
    try:
        fh = urllib.urlopen("http://www.google.com")
    except IOError:
        return False
    fh.close()
    return True


def start_check():
    """
    when program starts it checks for internet connectivity and installation of subliminal
    >>> start_check()  #when connected to internet and subliminal installation
    True

    :return: status whether start program or not
    """
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
        cli_menu()
    else:
        print "restart again after resolving given problems"
        sys.exit(0)