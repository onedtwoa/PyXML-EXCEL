import xml.dom.minidom as minidom
import xlsxwriter

def getTitles(xml):

    doc = minidom.parse(xml)
    node = doc.documentElement
    distributions = doc.getElementsByTagName("distributions")

    titles = []
    for distr in distributions:
        titleObj = distr.getElementsByTagName("label")[0]
        titleC = distr.getElementsByTagName("count")[0]
        titles.append((titleObj,titleC))

    agregResult = {}
    for title in titles:
        nodes = [title[0].childNodes, title[1].childNodes]
        for node in nodes[0]:
            if node.nodeType == node.TEXT_NODE:
                label = node.data
        for node in nodes[1]:
            if node.nodeType == node.TEXT_NODE:
                count = node.data
        if agregResult.get(label) == None:
            agregResult.update({label: int(count)})
        else:
            k = agregResult.pop(label)
            agregResult.update({label: int(count) + int(k) })

    return agregResult#.items()


if __name__ == "__main__":

    document = 'Reci.xml'

    label = getTitles(document).keys()
    count = getTitles(document).values()

    workbook = xlsxwriter.Workbook('label_count.xlsx')
    worlsheet = workbook.add_worksheet()

    worlsheet.write_column('A1', "label")
    worlsheet.write_column('A2', label)

    worlsheet.write_column('B1', "count")
    worlsheet.write_column('B2', count)

    workbook.close()