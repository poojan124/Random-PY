'''
    * scrape data from open directory. (all <a> in given page.)
    * support multiprocessing.
    * arguments:
        1. url to scrape.
        2. dirctory where you want to save files.
    * TODO:
        - add tqdm for multiprocessing. To display progess.
        - break dowm url constuction. (trivial)
        - automatically find files with given file type. Ex: video.(regex!?) 
'''

import os
import requests
import sys
from subprocess import call
from multiprocessing import Pool
from urllib.parse import unquote
from bs4 import BeautifulSoup as bsp

url = sys.argv[1]
_dir_ = 'data'
if len(sys.argv) >= 3:
    _dir_ = sys.argv[2]


def stacker(bob):
    stack = []
    for l in bob.find_all('a'):
        print("File: ", unquote(l['href']))
        # print('wget '+url+l.text)
        print("Download?: 'n' for No, 'e' for stop searching, anything else for Yes ",end= ' ')
        option = input().lower()
        if option == 'e':
            break
        elif option == 'n':
            continue
        else:
            stack.append('curl ' + url + l['href'] + ' -o ' + '"'+ unquote(l['href']) + '"' + ' --progress-bar')
    print(*stack, sep='\n')
    if input('Do you want to reset the list?. Y/N') == 'Y':
        return stacker(bob)
    return stack


def modified_call(*args, **kwargs):
    print("Started downloading ", args[0])
    call(*args, **kwargs)
    print("Finished downloading ", args[0])


if __name__ == '__main__':

    # win file system case insensitive. Check lower or your script will scream.
    if _dir_.lower() not in map(str.lower, os.listdir()):
        os.mkdir(_dir_)
    else:
        print("Directory named ", _dir_, " already exists. Saving into same dir.")
    os.chdir(_dir_)
    
    res = requests.get(url)
    bob = bsp(res.content, 'html.parser')
    stack = stacker(bob)

    if input("Do you want run multiprocess? y/n\n").lower() == 'y':
        stack = [x + ' -s' for x in stack] # add -s `silent` option for multiprocessing
        p = Pool(processes=3)
        p.map(modified_call, stack)
    else:
        _ = list(map(modified_call, stack))
