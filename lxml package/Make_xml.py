from lxml import etree, objectify
import datetime

FDSNStationXML = etree.Element("FDSNStationXML", xsi='http://www.w3.org/2001/XMLSchema-instance')
etree.SubElement(FDSNStationXML, "Source").text = "ljy"
etree.SubElement(FDSNStationXML, "Sender").text = "ljy"
etree.SubElement(FDSNStationXML, 'Module').text = 'ljy'
etree.SubElement(FDSNStationXML, 'ModuleURI').text = 'https://github.com/Junyi-Li96/LASIF-script'
etree.SubElement(FDSNStationXML, 'Created').text = str(datetime.datetime.now().replace(microsecond=0).isoformat())
etree.SubElement(FDSNStationXML, 'Network', code = 'LA', startDate='1970-01-01T00:00:00', endDate="2599-12-31T23:59:59", restrictedStatus="open")

# source = etree.SubElement(annotation, "source")
# etree.SubElement(source, "database").text = "COCO"
# etree.SubElement(source, "annotation").text = "COCO"
# etree.SubElement(source, "image").text = "COCO"
# etree.SubElement(source, "url").text = "http://test.jpg"
# size = etree.SubElement(annotation, "size")
# etree.SubElement(size, "width").text ='800' # 必须用string
# etree.SubElement(size, "height").text = '600'
# etree.SubElement(size, "depth").text = '3'
# etree.SubElement(annotation, "segmented").text = '0'
# key_object = etree.SubElement(annotation, "object")
# etree.SubElement(key_object, "name").text = 'person'
# bndbox = etree.SubElement(key_object, "bndbox")
# etree.SubElement(bndbox, "xmin").text = str(100)
# etree.SubElement(bndbox, "ymin").text = str(200)
# etree.SubElement(bndbox, "xmax").text = str(300)
# etree.SubElement(bndbox, "ymax").text = str(400)
# etree.SubElement(key_object, "difficult").text = '0'

doc = etree.ElementTree(FDSNStationXML)
doc.write("test.xml", pretty_print=True)