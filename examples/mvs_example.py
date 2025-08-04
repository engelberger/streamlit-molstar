import streamlit as st
from streamlit_molstar import st_molstar_mvs

st.title("MolViewSpec Example")

st_molstar_mvs(
    "https://raw.githubusercontent.com/molstar/molstar/master/examples/mvs/1cbs.mvsj",
    height="500px",
)
