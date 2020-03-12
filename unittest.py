from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import os
import easygui

def filename(file):
    filename = os.path.basename(file).split(".")[0]
    return filename

def dwgname(dwg):
    name = dwg.find_all('table')[1].find('font').text.split('\\')[-1].rstrip()
    return name

def dwgproblems(dwg):
    problems = dwg.find_all('table')[3].find('tr').find_next_siblings('tr')
    return problems

print('-- Select input file:')
path = easygui.fileopenbox(default="C://")

with open(path) as fp:
    # results = BS(fp).find(id="ResultsTable")
    results = BS(fp).find_all('table',id=re.compile('ErrDwg[0-9]*'))

print(len(results))
input()