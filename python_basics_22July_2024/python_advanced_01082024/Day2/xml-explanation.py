##################XML processing
>>> path = r"D:\handson\DAY2\data\example.xml"
>>> import xml.etree.ElementTree as ET
>>> tr = ET.parse(path)
>>>
>>> root = tr.getroot()
>>> type(root)
<class 'xml.etree.ElementTree.Element'>
>>> dir(root)
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'attrib', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']
>>> root.tag, root.attrib, root.text
('data', {}, '\n    ')
>>> #traversing
>>> #ex- get all ranks
>>> nn = root.findall("./country/rank")  # XPATH
>>> [n.text for n in nn]
['1', '4', '68']
>>> #XML -disadv - no DT, only string
>>> [int(n.text) for n in nn]
[1, 4, 68]
>>> #https://www.w3schools.com/xml/xpath_syntax.asp
>>>

########################
########more notes######
########################

>>> # // - search at any level, . - current ele
>>> # .. parent ...
>>> xn = root.findall(".//year/..[@name='Singapore']")
>>> xn
[<Element 'country' at 0x000001A29E692868>]
>>> root.findall(".//year")
[<Element 'year' at 0x000001A29E692728>, <Element 'year' at 0x000001A29E692908>, <Element 'year' at 0x000001A29E692A98>]
>>> root.findall(".//year/..")
[<Element 'country' at 0x000001A29E692688>, <Element 'country' at 0x000001A29E692868>, <Element 'country' at 0x000001A29E6929F8>]
>>> xn = root.findall(".//year/..[@name='Singapore']")
>>> xn
[<Element 'country' at 0x000001A29E692868>]
>>> [ n for n in root.findall(".//year/..") if n.attrib['name'] == 'Singapore']
[<Element 'country' at 0x000001A29E692868>]

https://docs.python.org/3/library/xml.etree.elementtree.html

2 disadvantages - no Data type, only string, need to learn XPATH