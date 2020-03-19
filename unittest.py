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

def fileselection(message, path):
    print(message)
    f = easygui.fileopenbox(title=str(message), default=str(path))
    if type(f) != str:
        if easygui.ynbox('No file selected. Do you want to continue?', 'Continue?', ('Yes', 'No')) == True:
            fileselection(message, path)
        else:
            sys.exit('Exiting program.')
    else:
        print(f)
    return f

sfile = fileselection('-- Select input file:', 'c://')

dfile = fileselection('-- Select output file:', 'c://')
