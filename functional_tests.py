__author__ = 'danielsiker'

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def user_can_start_a_list_and_retrieve_it_later(self):
        # lily wants to check out our cool new to-do list app
        # let's check it out, no?
        self.browser.get('http://localhost:8000')

        # she notices the silly title
        self.assertIn('Go At It', self.browser.title)
        self.fail('Finish the test!')

        # she's invited to enter a 'goat' item right away

        # she types "brew monkey tea" into a text box

        # when she hits enter, the page updates

        # there is still a text box (now empty) inviting her to add another item
        # she enters "drink monkey tea, slowly"

        # the page updates again, now she has 2 items on her list

        # lily sees our unique URL for her

        # she goes to that URL. and rejoices.
if __name__ == '__main__':
    unittest.main(warnings='ignore')