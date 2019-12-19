from lxml import etree

# Stations_parser = etree.HTMLParser(encoding='utf-8')
# Stations = etree.parse("lagou.html", parser=Stations_parser)

Stations = etree.parse("Station.html")
print(etree.tostring(Stations, encoding='utf-8').decode('utf-8'))
# Channals = Stations.xpath("//Site")
# for Channal in Channals:
#     print(etree.tostring(Channal, encoding='utf-8').decode('utf-8'))