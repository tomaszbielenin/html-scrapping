# Tasklist
# Multiple files handling - one or multiple spreadsheets (df.to_excel - append to existing)

# import bottleneck as bn # import bn to supress Bottleneck unit testing error 
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import sys
import os
import easygui

# File selection dialog with choice handling
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

def filename(file):
    filename = os.path.basename(file).split(".")[0]
    return filename

def outfile(file):
    dfile = sfolder + '\\' + filename(file) + '.xlsx'
    return dfile

def dwgname(dwg):
    name = dwg.find_all('table')[1].find('font').text.split('\\')[-1].rstrip()
    return name

def dwgproblems(dwg):
    problems = dwg.find_all('table')[3].find('tr').find_next_siblings('tr')
    return problems

# Core scrapping function
def filescrapper(file):
    with open(file) as fp:
        results = BS(fp,features="lxml").find_all('table',id=re.compile('ErrDwg[0-9]*')) #lxml parser specified to avoid additional messages

    i=0
    dct = {}
    for dwg in results:
        dproblems = dwgproblems(dwg)
        dname = dwgname(dwg)
        for tr in dproblems:
            if tr.find_all('table'):
                itemname = tr.find('td').font.text
                for itr in tr.find('table').find('tr').find_next_siblings('tr'): 
                    if len(itr.find_all('td'))>1:
                        dct['lst_%s' % (str(i))] = []
                        dct['lst_%s' % (str(i))].append(dname)
                        dct['lst_%s' % (str(i))].append(itemname)
                        for td in itr.find_all('td'):
                            dct['lst_%s' % (str(i))].append(td.font.text.rstrip().lstrip())
                        i+=1 
            elif len(tr.find_all('td'))==1:
                dct['lst_%s' % (str(i))] = []
                dct['lst_%s' % (str(i))].append(dname)
                dct['lst_%s' % (str(i))].append(tr.td.font.text.rstrip().lstrip())
                i+=1    
            else:
                dct['lst_%s' % (str(i))] = []
                dct['lst_%s' % (str(i))].append(dname)
                for td in tr.find_all('td'):
                    dct['lst_%s' % (str(i))].append(td.font.text.rstrip().lstrip())
                i+=1

    for key in dct:
        while len(dct[key])<5:
            dct[key].append('')

    drawings = []
    items = []
    properties = []
    current = []
    standard = []
        
    for key in dct:
        drawings.append(dct[key][0])
        items.append(dct[key][1])
        properties.append(dct[key][2])
        current.append(dct[key][3])
        standard.append(dct[key][4])
            
    df = pd.DataFrame({'Drawing' : drawings, 'Item': items, 'Property': properties, 'Current' : current, 'Standard' : standard})
    with pd.ExcelWriter(dfile) as writer:
        df.to_excel(writer, sheet_name=filename(file), index=False)

# Interactive and batch mode handling
if len(sys.argv) == 1:
    sfile = fileselection('-- Select input file:', 'c://')
    sfolder = os.path.dirname(sfile)
    # dfile = fileselection('-- Select output file:', 'c://')
    dfile = outfile(sfile)
    filescrapper(sfile)
elif len(sys.argv) == 2:
    sfolder = str(sys.argv[1]) # source folder
    # sfolder = 'C:\Scripting\Git\html-scrapping'
    for sfile in os.listdir(sfolder):
        if sfile.lower().endswith(".htm"):
            dfile = outfile(sfile)
            print('Scrapping ' + sfolder + '\\' + sfile)
            filescrapper(sfolder + '\\' + sfile) # Added sfolder to run script from any location
            print(dfile)
print()
print('Done!')