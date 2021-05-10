from pageObjects.basePO import PO
from selenium.webdriver.common.keys import Keys
import time

class DuckDuckGoPO(PO):
    
    def open(self):
        self.driver.get('https://duckduckgo.com/')

    def get_title(self):
        return self.driver.title

    def search(self, query):
        searchbar = self.find_elem('[id=search_form_input_homepage]')
        searchbar.send_keys(query)
        searchbar.send_keys(Keys.ENTER)

    def open_briefly(self):
        time.sleep(2)
        ref = self.driver.find_element_by_css_selector('a.js-result-title-link[href^="https://briefly"]')
        ref.click()