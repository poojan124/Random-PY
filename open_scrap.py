'''
    ex : python open_scrap.py LINK_TO_OPEN_DIRECTORY
    TODO :
        -> Add another variable for concurrent multiple download.
            {
                - spawn one terminal for each download.? (1)
                - Hide terminal? (option?)
                - show size of file before download and check once downloded file size. ?
            }
    
'''

import os
import requests
import sys
from subprocess import call
from bs4 import BeautifulSoup as bsp

url = sys.argv[1]

if 'data' not in os.listdir():
    os.mkdir('data')

res = requests.get(url)
bob = bsp(res.content, 'html.parser')

os.chdir('./data')

class scrapper():
    
    def __init__(slef,origin,multi=False):
        self.origin = origin
        self.multi = multi

    def scrap(self, flag):

#bob is response object
def stacker(bob):
    stack = []
    for l in bob.find_all('a'):
        print(l['href'])
        print("this will be the file", url+l['href'])
        # print('wget '+url+l.text)
        print("Download yes or no y/n: ",end= ' ')
        if input() == 'y':
            stack.append('wget '+url+l['href']+" -q --show-progress")
        else:
            pass
    for st in stack:
        print(st)
    print("-----------")
    print("Do you like this or you want to overwrite this YES TO OVERWRITE : ",end='')
    if input()=='y':
        stacker(bob)
    else:
        return stack

stack = stacker(bob)
for s in stack:
    print("file is downloading for this link ",s)
    call(s,shell=True)
