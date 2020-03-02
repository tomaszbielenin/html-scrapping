from bs4 import BeautifulSoup

with open('C:/Scripting/Git/html-scrapping/d0178777.HTM') as fp:
    results = BeautifulSoup(fp).find(id="ResultsTable")

dwgs = results.find_all('font', {'class':'labelText4Blue'})
dwgnames = []
for dwg in dwgs:
    dwgnames.append(dwg.text)

dwg = results.find(text='xR200-E29-AAP100.dwg')
table_1 = dwg_1.find_parents('table')
len(results.find('table'))
soup.find_all('font', {'class':'valueText2'})

dwg = results.find('font', {'class':'labelText4Blue'})
dwgtable = dwg.find_parent('table')
dwgproblems = dwgtable.find_next_sibling('table')
dwgproblems.find_all('font',{'class':'valueText2'})
dwg.find_all(text='A-DELT')