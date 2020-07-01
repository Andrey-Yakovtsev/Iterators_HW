import json
import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')

def get_country_official_name():
    with open('countries.json', encoding='utf-8') as countries_data:
        country = json.load(countries_data)
        countries_official_names_list = []
        for item in country:
            countries_official_names_list.append(item['name']['official'])
    return countries_official_names_list



class WikiIterator:

    def __init__(self, start=0, end=len(get_country_official_name())-1):
        self.start = start #взять объект оп индерсу в списке
        self.end = end # последний по индексу
        self.current = start
        self.country_list = get_country_official_name()

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        self.link = self.get_link(self.country_list[self.current])
        return {self.country_list[self.current]: self.link}

    def get_link(self, country):

        try:
            page_py = wiki_wiki.page(country)
            return page_py.fullurl

        except KeyError:
            return ('Has no link in Wiki')


classes_countries_links = []
for item in WikiIterator():
    classes_countries_links.append(item)

with open('classes_countries_links.json', 'w') as fi:
    json.dump(classes_countries_links, fi, ensure_ascii=False, indent=2)
