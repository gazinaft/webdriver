class PO:
    def __init__(self, driver):
        self.driver = driver
    
    def find_elem(self, text):
        return self.driver.find_element_by_css_selector(text)
