import streamlit as st
import pandas as pd

test = pd.DataFrame(
    [
        pd.Series(['a', 1, 'c'], name='val1', dtype=str),
        pd.Series(['d', 2, 'e'], name='val2', dtype=str),
        pd.Series(['f', 2, 'h'], name='val2', dtype=str),
    ]
)

# test = test['val1']

print(test)

st.write("Hi. Editted. Again. And Again.")
st.write(test)
