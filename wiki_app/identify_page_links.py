import re


def identify_page_links(page_content):
    links = re.findall(r'\[(.*?) *\]', page_content)
    return links
