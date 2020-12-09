import streamlit as st
import pandas as pd


st.set_page_config('Tax Brackets from 1913-2020', page_icon=":money_with_wings:", layout="wide")

f  = 'fed_individual_rate_history_nominal_1913_2020.csv'

st.write(pd.read_csv(f, index_col=0))
