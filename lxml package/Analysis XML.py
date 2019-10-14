from lxml import etree

text = '''
<scores>
    <student id="1">
        <name>ljy</name>
        <course>python</course>
        <score>100</score>
    </student>
    <student id="2">
        <name>beileye</name>
        <course>xml</course>
        <score>101</score>
    </student>
    <student id="3">
        <name>xiaobeile</name>
        <course>c</course>
        <score>102</score>
    </student>
</scores>
'''

def parse_text():
    text_element = etree.HTML(text)
    print(etree.tostring(text_element, encoding='utf-8').decode('utf-8'))

def parse_file():
    file_element = etree.parse("Inter DTD")
    print(etree.tostring(file_element, encoding='utf-8').decode('utf-8'))

def parse_html():
    parse =  etree.HTMLParser(encoding='utf-8')
    html_element = etree.parse("lagou.html", parser=parse)
    print(etree.tostring(html_element, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_file()
    # parse_html()
    # parse_text()
