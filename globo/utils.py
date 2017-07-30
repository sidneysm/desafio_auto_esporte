from bs4 import BeautifulSoup, element


def split_elements(description):
    return [elem for elem in description.contents
            if type(elem) is not element.NavigableString
            and (elem.name != 'p' or len(elem.get_text().strip()) != 0)]


def parse_element_to_json(element):
    content = {}
    if element.img:
        content = {
            "type": "image",
            "content": element.img.get('src')
        }
        return content
    elif element.ul:
        content = {
            "type": "links",
            "content": [link.get('href') for link in element.ul.find_all('a')]
        }
        return content
    elif len(element.get_text().strip()) != 0:
        content = {
            "type": "text",
            "content": element.get_text().strip()
        }
        return content
