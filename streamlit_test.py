import streamlit as st
import pandas as pd

test = pd.DataFrame(
    pd.Series(['a', 1, 'c'], name='val1', dtype=str),
)

test = test['val1']

print(test)

st.write("Hi. Editted. Again.")
st.write(test)
