from xml.dom import minidom

def getxml():
    xmlfile = minidom.parse('Untitled.xml')

    clientinfo = xmlfile.getElementsByTagName('422')


if __name__ == "__main__":
    getxml()