import xlrd
from lxml import etree

root = etree.Element('network')
root.set('name', 'Network')
tree = etree.ElementTree(root)
name = etree.Element('nodes')
root.append(name)
wb = xlrd.open_workbook("input.xls")
sh = wb.sheet_by_index(0)

for row in range(1, sh.nrows):
    val = sh.row_values(row)
    element = etree.SubElement(name, 'node')
    element.set('id', str(int(val[0])))
    element.set('x', str(val[1]))
    element.set('y', str(val[2]))
print etree.tostring(root,pretty_print=True)
