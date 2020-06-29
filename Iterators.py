import json
import wikipediaapi


def get_country_official_name(country_count):
    with open('countries.json', encoding='utf-8') as countries_data:
        country = json.load(countries_data)
        countries_official_names_list = []
        for i in range(country_count):
            countries_official_names_list.append(country[i]['name']['official'])
            # print(countries_official_names_list)
        return countries_official_names_list



wiki_wiki = wikipediaapi.Wikipedia('en')
countries_links_list = []
for country in get_country_official_name(10):
    try:
        page_py = wiki_wiki.page(country)
        country_item = {'country': country,  'url': page_py.fullurl}
        print(country_item)
    except KeyError:
        country_item = {'country': country,  'url': 'No link'}
        print(country_item)

    countries_links_list.append(country_item)


with open('countries_links.json', 'w') as fi:
    json.dump(countries_links_list, fi, ensure_ascii=False, indent=2)