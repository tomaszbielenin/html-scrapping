from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import sys
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
sfile = easygui.fileopenbox(title='Select input file:', default="C://")
if type(sfile) != str:
    sys.exit('No input file selected. Exiting program.')
else:
    print(sfile)

print('-- Select output file:')
dfile = easygui.fileopenbox(title='Select output file:', default=os.path.dirname(sfile)) # Can't say why it shows parent folder
if type(dfile) != str:
    sys.exit('No output file selected. Exiting program.')
else:
    print(dfile)