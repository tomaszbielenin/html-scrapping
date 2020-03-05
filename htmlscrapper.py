# Import libraries
# Body
# Save to excel

# import easygui as eg

from bs4 import BeautifulSoup as BS
import re

with open('C:/Scripting/Git/html-scrapping/d0178777.HTM') as fp:
    results = BS(fp).find(id="ResultsTable")

dwgs = results.find_all('font', {'class':'labelText4Blue'})
dwgnames = []
for dwg in dwgs:
    dwgnames.append(dwg.text.split('\\')[-1].rstrip())

# from pandas import DataFrame
import pandas as pd
# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# df = pd.DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})
# dwgs = []
problems = list(range(0,len(dwgnames)))
names = list(range(0,len(dwgnames)))
properties = list(range(0,len(dwgnames)))
values = list(range(0,len(dwgnames)))

df = pd.DataFrame({'Files': dwgnames, 'Type': problems, 'Data': names, 'Property': properties, 'Current Value': values})
df

df.to_excel('Filename.xlsx', sheet_name='SheetName', index=False)

# Save to csv
# f = open('example.csv','w')
# f.write("display,variable x")
# f.close()

# Library to work with excel
# import xlwt

# def output(filename, sheet, list1, list2, x, y, z):
#     book = xlwt.Workbook()
#     sh = book.add_sheet(sheet)

#     variables = [x, y, z]
#     x_desc = 'Display'
#     y_desc = 'Dominance'
#     z_desc = 'Test'
#     desc = [x_desc, y_desc, z_desc]

#     col1_name = 'Stimulus Time'
#     col2_name = 'Reaction Time'

#     #You may need to group the variables together
#     #for n, (v_desc, v) in enumerate(zip(desc, variables)):
#     for n, v_desc, v in enumerate(zip(desc, variables)):
#         sh.write(n, 0, v_desc)
#         sh.write(n, 1, v)

#     n+=1

#     sh.write(n, 0, col1_name)
#     sh.write(n, 1, col2_name)

#     for m, e1 in enumerate(list1, n+1):
#         sh.write(m, 0, e1)

#     for m, e2 in enumerate(list2, n+1):
#         sh.write(m, 1, e2)

#     book.save(filename)