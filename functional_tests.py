__author__ = 'danielsiker'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # lily wants to check out our cool new to-do list app
        # let's check it out, no?
        self.browser.get('http://localhost:8000')

        # she notices the silly title
        self.assertIn('Go At It', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', header_text)

        # she's invited to enter a 'goat' item right away
        inputbox = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Go At It item'
        )

        # she types "brew monkey tea" into a text box
        inputbox.send_keys('brew monkey tea')

        # when she hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')  # find_elementS returns a list which may be empty
        self.assertIn('1. brew monkey tea', [row.text for row in rows])

        # there is still a text box (now empty) inviting her to add another item
        # she enters "drink monkey tea, slowly"
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys('drink monkey tea, slowly')
        inputbox.send_keys(Keys.ENTER)


        # the page updates again, now she has 2 items on her list
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')  # find_elementS returns a list which may be empty
        self.assertIn('1. brew monkey tea', [row.text for row in rows])
        self.assertIn(
            '2: drink monkey tea, slowly',
            [row.text for row in rows]
        )

        # lily sees our unique URL for her

        # she goes to that URL. and rejoices.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')