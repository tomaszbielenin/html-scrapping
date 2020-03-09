# Add file naming
# Add batch mode
# Add some UI

from bs4 import BeautifulSoup as BS
import pandas as pd
import re

# with open('C:/Scripting/Git/html-scrapping/ErrDwg25.HTM') as fp:
with open('C:/Scripting/Git/html-scrapping/d0178772.HTM') as fp:
    # results = BS(fp).find(id="ResultsTable")
    results = BS(fp).find_all('table',id=re.compile('ErrDwg[0-9]*'))

def dwgname(dwg):
    name = dwg.find_all('table')[1].find('font').text.split('\\')[-1].rstrip()
    return name

def dwgproblems(dwg):
    problems = dwg.find_all('table')[3].find('tr').find_next_siblings('tr')
    return problems

# path = r'C:/Scripting/Git/html-scrapping/dwgs.xls'
# writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
i=0
dct = {}
for dwg in results:
    dproblems = dwgproblems(dwg)
    dname = dwgname(dwg)
    for tr in dproblems:
        if tr.find_all('table'):
            itemname = tr.find('td').font.text
            for itr in tr.find('table').find('tr').find_next_siblings('tr'): 
                # print('There\'s a nested table')
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
            # dct['lst_%s' % (str(i))].append(itemname)
            dct['lst_%s' % (str(i))].append(tr.td.font.text.rstrip().lstrip())
            i+=1    
        else:
            dct['lst_%s' % (str(i))] = []
            dct['lst_%s' % (str(i))].append(dname)
            # dct['lst_%s' % (str(i))].append(itemname)
            for td in tr.find_all('td'):
                dct['lst_%s' % (str(i))].append(td.font.text.rstrip().lstrip())
            i+=1
        # if not tr.find_all('table'):
        #     dct['lst_%s' % (troubles.index(tr)+1)] = []
        #     for td in tr.find_all('td'):
        #         dct[('lst_%s' % (troubles.index(tr)+1))].append(td.font.text.rstrip().lstrip())
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
df.to_excel('d0178772.xlsx', sheet_name='Problems', index=False)
    # writer.save()
    # writer.close()
# dwgname = results[25].find_all('table')[1].find('font').text.split('\\')[-1].rstrip() # dwgname
# troubles = results[25].find_all('table')[3].find('tr').find_next_siblings('tr') # problemtable

lst = []
for tr in troubles:
    if len(tr.find_all('td'))==1:
        # print(troubles.index(tr))
        lst.append(tr.td.font.text.rstrip().lstrip())

for tr in troubles:
    if len(tr.find_all('table'))==0:
        for td in tr.find_all('td'):
            print(td.font.text)

dct = {}
for tr in troubles:
    if tr.find_all('table'):
        dct['lst_%s' % (troubles.index(tr)+1)] = []
        for td in tr.find_all('td'):
            dct[('lst_%s' % (troubles.index(tr)+1))].append(td.font.text.rstrip().lstrip())

dct = {}
for tr in troubles:
    if not tr.find_all('table'):
        dct['lst_%s' % (troubles.index(tr)+1)] = []
        for td in tr.find_all('td'):
            dct[('lst_%s' % (troubles.index(tr)+1))].append(td.font.text.rstrip().lstrip())

for key in dct:
    while len(dct[key])<2:
        dct[key].append('')

items = []
issues = []
for key in dct:
    items.append(dct[key][0])
    issues.append(dct[key][1])

import pandas as pd

df = pd.DataFrame({'Item': items, 'Issue': issues})
df

df.to_excel('Filename.xlsx', sheet_name=dwgname, index=False)


dwgs = results.find_all('font', {'class':'labelText4Blue'})
dwgnames = []
for dwg in dwgs:
    dwgnames.append(dwg.text.split('\\')[-1])

dwgs[0].text.split('\\')[-1]

dwg = dwgs[0]
dwgtable = dwg.find_parents('table')

dwg = results.find('font', {'class':'labelText4Blue'})
dwgtable = dwg.find_parent('table')
dwgproblems = dwgtable.find_next_sibling('table')
trs = dwgproblems.tbody.find('table')

lst = []
for tr in trs:
    for font in tr.find_all('font'):
        lst.append(font.text.lstrip().rstrip())

dwgproblems.find_all('font',{'class':'valueText2'})
dwg.find_all(text='A-DELT')