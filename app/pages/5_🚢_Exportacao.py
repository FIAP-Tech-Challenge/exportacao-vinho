import streamlit as st

from classes import graphs as g
from classes import structure as s
from classes import functions as f

f.config_streamlit()
df = f.load_data()
s.header()

s.tab_intro(df)
