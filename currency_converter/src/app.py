import streamlit as st
from src.utils.constants import CURRENCIES
from src.utils.utils import get_last_update
from src.service.currency import get_exchange_rate, convert_currency

st.markdown("# :dollar: Currency Converter")

from_currency = st.selectbox("from currency: ", CURRENCIES)
target_currency = st.selectbox("target currency: ", CURRENCIES)
amount = st.number_input("amount to convert", min_value=0.0, step=0.1)

rate = get_exchange_rate(from_currency, target_currency)
time_ago = get_last_update(from_currency)

if rate is None:
    st.error("Exchange rate not found")
else:
    convert_amount = convert_currency(amount, rate)
    st.success(f"Exchange rate: {rate} (Last updated: {time_ago})", icon="✅")

    c1, c2, c3 = st.columns(3)

    c1.metric("Base Currency", f"{amount:.2f} {from_currency}")
    c2.metric("", "→")
    c3.metric("Target Currency", f"{convert_amount:.2f} {target_currency}")
