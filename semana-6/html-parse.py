from html.parser import HTMLParser

class MyParser(HTMLParser):
    """ print todos links das tags a"""
    def handle_startendtag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = MyParser()
parser.feed(html)