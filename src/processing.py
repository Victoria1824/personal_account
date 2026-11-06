from datetime import datetime

def filter_by_state(list_of_dictionaries: [str], mean_key='EXECUTED') -> [str]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_dictionaries = []
    for item_dict in list_of_dictionaries:
        if item_dict.get('state') == mean_key:
            new_dictionaries.append(item_dict)
    return new_dictionaries

list_new_dictionaries = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


def sort_by_date(list_of_dictionaries: [str], sort_order='True') -> [str]:
    """Возвращает новый список, отсортированный по дате"""
    is_reverse = True if sort_order == 'False' else False

    return sorted(list_of_dictionaries, key=lambda x: datetime.fromisoformat(x['date']), reverse=is_reverse)

sort_date = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

