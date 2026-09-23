"""
 Продолжаем работу над виджетом банковских операций клиента.
 В этом задании вам предстоит использовать Git для сохранения истории развития вашего проекта.
 Реализуйте новый функционал, делая небольшие коммиты.
"""

import masks


def mask_account_card(mask_card: str) -> str:
    """Зашифровка карты или счета"""
    letters = ""
    numbers = ""
    for i in mask_card:
        if i.isdigit():
            numbers += i
    numbers_len = len(numbers)
    if numbers_len == 16:
        card_number = masks.get_mask_card_number(mask_card)
        return card_number
    elif numbers_len == 20:
        get_mask = masks.get_mask_account(mask_card)
        return get_mask


input_from_user = input("Введите свой номер карты или счета:")
returned_value = mask_account_card(input_from_user)
print(returned_value)

def get_date(date: str) -> str:
    """2024-03-11T02:26:18.671407"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


date = get_date('2024-03-11T02:26:18.671407')


