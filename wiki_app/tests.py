import unittest
from wiki.wiki_app.identify_page_links import identify_page_links


class TestTransportPageLinks(unittest.TestCase):
    def test_none_present(self):
        test_text = '"Lorem ipsum dolor sit amet'
        self.assertEqual(identify_page_links(test_text), [])

    def test_single_present(self):
        test_text = '"Lorem [ipsum] dolor sit amet'
        self.assertEqual(identify_page_links(test_text), ['ipsum'])

    def test_multiple_present(self):
        test_text = '"Lorem [ipsum] dolor sit [amet]'
        self.assertEqual(identify_page_links(test_text), ['ipsum', 'amet'])