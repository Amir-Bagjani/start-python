import streamlit as st
from src.main import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

st.title("Password Generator")

option = st.radio(
    "Select a password generator: ",
    ("Random Password", "Memorable Password", "Pin Password"),
)

generator = None

if option == "Pin Password":
    length = st.slider("Select the length of the pin:", 4, 10)
    generator = PinGenerator(length=length)
elif option == "Random Password":
    length = st.slider("Select the length of the random password:", 4, 10)
    random_options = st.multiselect("select the options:", ("numbers", "symbols"))
    generator = RandomPasswordGenerator(
        length=length,
        includes_number="numbers" in random_options,
        includes_symbol="symbols" in random_options,
    )
else:
    length = st.slider("Select the length of the number of words:", 4, 10)
    capitalize = st.checkbox("should be capitalized?")
    separator = st.selectbox(
        "select the separator:",
        ("-", "/", ".", "*"),
    )
    generator = MemorablePasswordGenerator(
        words_number=length,
        capitalize=capitalize,
        separator=separator,
    )


if st.button("Generate", type="primary"):
    st.code(generator.generate())
