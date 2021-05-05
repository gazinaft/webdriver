from pageObjects.basePO import PO
from selenium.webdriver.common.keys import Keys

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
        ref = self.find_elem("a[href^='https://briefly.ru']")
        ref.click()