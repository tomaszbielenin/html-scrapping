# Add file naming
# Add batch mode
# Add some UI
# df.to_excel - append to existing
# easygui windows descriptions
# handling exception - if easygui open is calcelled
# Multiple files handling - one or multiple spreadsheets 

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
sfile = easygui.fileopenbox(default="C://")
print(sfile)
print('-- Select output file:')
dfile = easygui.fileopenbox(default=os.path.dirname(sfile)) # Can't say why it shows parent folder
print(dfile)

with open(sfile) as fp:
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
    df.to_excel(writer, sheet_name=filename(sfile), index=False) # Returns 'No Bottleneck unit testing available' when run from terminal
