from pageObjects.basePO import PO

class BrieflyPO(PO):

    def get_year(self):
        return self.find_elem('span.date').text

    def get_author(self):
        return self.find_elem('div.breadcrumb__name').text

    def get_title(self):
        return self.find_elem('span.main').text
