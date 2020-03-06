from bs4 import BeautifulSoup as BS
import pandas as pd
import re

with open('C:/Scripting/Git/html-scrapping/d0178777.HTM') as fp:
    # results = BS(fp).find(id="ResultsTable")
    results = BS(fp).find_all('table',id=re.compile('ErrDwg[0-9]*'))

def dwgname(dwg):
    name = dwg.find_all('table')[1].find('font').text.split('\\')[-1].rstrip()
    return name

def dwgproblems(dwg):
    problems = dwg.find_all('table')[3].find('tr').find_next_siblings('tr')
    return problems

path = r'C:/Scripting/Git/html-scrapping/dwgs.xls'
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
for dwg in results:
    dct = {}
    troubles = dwgproblems(dwg)
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
    df = pd.DataFrame({'Item': items, 'Issue': issues})
    df.to_excel(writer, sheet_name=dwgname(dwg), index=False)
    writer.save()
    writer.close()
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