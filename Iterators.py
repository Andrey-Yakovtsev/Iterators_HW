import json
import wikipediaapi


def get_country_official_name():
    with open('countries.json', encoding='utf-8') as countries_data:
        country = json.load(countries_data)
        countries_official_names_list = []
        for item in country:
            countries_official_names_list.append(item['name']['official'])
        return countries_official_names_list



wiki_wiki = wikipediaapi.Wikipedia('en')
countries_links_list = []
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
for country in get_country_official_name():
    try:
        page_py = wiki_wiki.page(country)
        country_item = {'country': country,  'url': page_py.fullurl}
    except KeyError:
        country_item = {'country': country,  'url': 'No link'}

    countries_links_list.append(country_item)


with open('countries_links.json', 'w') as fi:
    json.dump(countries_links_list, fi, ensure_ascii=False, indent=2)
#
# class WikiIterator:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start - 1
#         self.session = requests.session()
#
#     def __iter__(self, country):
#         self.country = country
#         return country_link
#
#     def __next__(self):


