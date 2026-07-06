import requests
from typing import Optional
from cachetools import cached, TTLCache

ttl_cache = TTLCache(maxsize=100, ttl=300)


@cached(ttl_cache)
def get_exchange_rate(
    base_currency: str,
    target_currency: str,
) -> Optional[float]:
    url = "https://api.exchangerate-api.com/v4/latest/" + base_currency
    try:
        res = requests.get(url).json()
        return float(res["rates"][target_currency])
    except Exception as error:
        print(error)
        return None


def convert_currency(amount: float, rate: float) -> float:
    return amount * rate
