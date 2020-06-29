import json
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
# countries_links_list = []
#
# for country in get_country_official_name():
#     try:
#         page_py = wiki_wiki.page(country)
#         country_item = {'country': country,  'url': page_py.fullurl}
#     except KeyError:
#         country_item = {'country': country,  'url': 'No link'}
#
#     countries_links_list.append(country_item)




class WikiIterator:

    def __init__(self, start=int, end=int):
        self.start = start
        self.end = end
        self.current = start - 1 #пока нигде не применяю


    def __iter__(self):
        return self

    def __next__(self):
        return self

    def get_country_official_name(self, start, end):
        with open('countries.json', encoding='utf-8') as countries_data:
            country = json.load(countries_data)
            countries_official_names_list = []
            for i in range(start, end):
                countries_official_names_list.append(country[i]['name']['official'])
                return countries_official_names_list



for item in WikiIterator.get_country_official_name(1, 10, 11):
    print(item)
'''
в списке стран бежим по индексу
Берем название и суем его в апи вики для получения ссылки
полученый результат собираем в словарь: Страна - ссылка
словарь аппендим в список
Список дампим в Джсон - готово
'''

    # with open('countries_links.json', 'w') as fi:
    #     json.dump(countries_links_list, fi, ensure_ascii=False, indent=2)
