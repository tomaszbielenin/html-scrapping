from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import os
import easygui

def filename(file):
    filename = os.path.basename(file).split(".")[0].join()
    return filename

def dwgname(dwg):
    name = dwg.find_all('table')[1].find('font').text.split('\\')[-1].rstrip()
    return name

def dwgproblems(dwg):
    problems = dwg.find_all('table')[3].find('tr').find_next_siblings('tr')
    return problems

print('-- Select input file:')
sf = easygui.fileopenbox(default="C://")
print(sf)
print('-- Select output file:')
df = easygui.fileopenbox(default=os.path.dirname(sf)) # Can't say why it shows parent folder

with open(sf) as fp:
    results = BS(fp,features="lxml").find_all('table',id=re.compile('ErrDwg[0-9]*')) #lxml parser specified to avoid additional messages
