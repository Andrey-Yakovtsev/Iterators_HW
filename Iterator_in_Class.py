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

    def __init__(self, object, start=int, end=int):
        self.start = start
        self.end = end
        self.current = start - 1 #пока нигде не применяю
        self.object = object

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start





for item in WikiIterator(get_country_official_name()):
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

# print(get_country_official_name())