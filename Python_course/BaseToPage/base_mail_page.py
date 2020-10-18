class Field:
    def __init__(self, choose):
        self.choose = choose

    get_the_number_of_chouse = "[data-deselect*='Клік, щоб видалити']"
    for_hoo = "div.multiselect__tags:nth-child(2)"

    def clicker(self, chouse):
        result = f"#multiselect_multy_container > div > div > div.multiselect__content-wrapper > ul > li:nth-child({chouse}) > span > span"
        return result