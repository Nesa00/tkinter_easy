import xml.etree.ElementTree as ET
# program used to change language
filename = "language.xml"
xmlTree = ET.parse(filename)
rootElement = xmlTree.getroot()
def change_lang(name):
    for element in rootElement.findall("setup"):
        #Find the book that has title as 'Python Tutorial'
        if element.find('title').text == 'language':
            #Change the price
            element.find('language').text = name
    #Write the modified xml file.        
    xmlTree.write(filename,encoding='UTF-8',xml_declaration=True)

def read__ini(file):
    print("no")
