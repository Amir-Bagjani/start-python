from src.utils.utils import get_user_choice, get_user_amount
from src.service.currency import get_exchange_rate, convert_currency


def convert_handler():
    source_currency = get_user_choice("\nPlease enter the base currency (q to quit): ")
    if source_currency is None:
        print("Goodbye")
        return "break"

    target_currency = get_user_choice(
        "\nPlease enter the target currency (q to quit): "
    )
    if target_currency is None:
        print("Goodbye")
        return "break"

    amount = get_user_amount("\nPlease enter the amount (q to quit): ")
    if target_currency is None:
        print("Goodbye")
        return "break"

    rate = get_exchange_rate(source_currency, target_currency)

    if rate is not None and amount is not None:
        exchanges_amount = convert_currency(amount, rate)
        print(f"{amount} {source_currency} is {exchanges_amount} {target_currency}")
