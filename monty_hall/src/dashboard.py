import streamlit as st
import pandas as pd
import time
from main import simulate_game

st.title("Monty Hall Simulation")

num_game = st.number_input(
    "Enter number of games to simulate",
    min_value=10,
    max_value=100000,
    value=100,
    step=10,
)

col1, col2 = st.columns(2)

col1.subheader("Win percent (No Switch)")
col2.subheader("Win percent (Switch)")

chart1 = col1.empty()
chart2 = col2.empty()

wins_switch = 0
wins_not_switch = 0

data1 = []
data2 = []

for i in range(num_game):
    not_switch, switch = simulate_game(1)

    wins_switch += switch
    wins_not_switch += not_switch

    data1.append(wins_not_switch / (i + 1))
    data2.append(wins_switch / (i + 1))

    chart1.line_chart(pd.DataFrame(data1, columns=["No Switch"]))
    chart2.line_chart(pd.DataFrame(data2, columns=["Switch"]))

    time.sleep(0.01)