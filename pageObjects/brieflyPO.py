from pageObjects.basePO import PO

class BrieflyPO(PO):

    def get_year():
        return self.find_elem('span.date')

    def get_author():
        return self.find_elem('div.breadcrumb__name')

    def get_title():
        return self.find_elem('span.main')
