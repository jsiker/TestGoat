__author__ = 'danielsiker'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table_list(self, row_text):
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr') ###### FIND_ELEMENTSSSSSS for multiples####
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # lily wants to check out our cool new to-do list app
        # let's check it out, no?
        self.browser.get(self.live_server_url)

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
        lily_list_url = self.browser.current_url
        self.assertRegex(lily_list_url, '/lists/.+')
        self.check_for_row_in_table_list('1: brew monkey tea')

        # there is still a text box (now empty) inviting her to add another item
        # she enters "drink monkey tea, slowly"
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys('drink monkey tea, slowly')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, now she has 2 items on her list
        self.check_for_row_in_table_list('2: drink monkey tea, slowly')
        self.check_for_row_in_table_list('1: brew monkey tea')


        # new user bella comes to the site

        ## we use a new browser session, to make sure that none of lily's data persists
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # bella visits the page, no sign of lily
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('brew monkey tea', page_text)
        self.assertNotIn('play with monkey', page_text)

        # bella starts a new list
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys('doggy bags')
        inputbox.send_keys(Keys.ENTER)

        # bella gets her own url
        bella_list_url = self.browser.current_url
        self.assertRegex(bella_list_url, '/lists/.+')
        self.assertNotEqual(lily_list_url, bella_list_url)

        # no trace of lily's stuff
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('brew monkey tea', page_text)
        self.assertIn('doggy bags', page_text)
        # self.fail('Finish the test!')