"""
 IT-отдел крупного банка делает новую фичу для личного кабинета клиента.
 Это виджет, который показывает несколько последних успешных банковских операций клиента.
 Вам доверили реализовать этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.

 Реализуйте в этом модуле две функции:
 Функцию маскировки номера банковской карты
 get_mask_card_number
 Функцию маскировки номера банковского счета
 get_mask_account
"""

def get_mask_card_number(card_number:[str]) -> str:
    """ Функция для маскировки номера банковской карты """
    new_card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        return "Вы допустили ошибку, попробуйте ввести номер карты еще раз."

    for i in new_card_number:
        if not i.isdigit():
            return("Вы ввели не верный формат номера карты.")  # если ввод состоит не из цифр

    new_format_to_return = (new_card_number[:4] + " " + new_card_number[4:6] + "**" + " " + "****" + " " + new_card_number[-4:])
    return new_format_to_return


input_from_user = input("Введите свой номер карты:")
returned_value = get_mask_card_number(input_from_user)
print(returned_value)


def get_mask_account(account_number: str) -> str:
    """  Функция для маскировки номера банковского счета """
    new_account_number = account_number.replace(" ", "")
    if len(new_account_number) != 20:
        return "Номер счета не должен содержать больше 20 цифр. Попробуйте ещё раз."
    for i in new_account_number:
        if not i.isdigit():
            return("Вы ввели не верный формат номера счета.")

    return f"**{account_number[-4:]}"

input_from_user_account = input("Введите свой номер счета:")
returned_value = get_mask_account(input_from_user_account)
print(returned_value)




