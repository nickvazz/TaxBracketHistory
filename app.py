import streamlit as st
import pandas as pd


f  = 'fed_individual_rate_history_nominal_1913_2020.csv'

st.write(pd.read_csv(f, index_col=0))
