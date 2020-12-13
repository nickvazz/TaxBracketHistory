import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
import matplotlib as mpl
import seaborn as sns
sns.set()

st.set_page_config('Tax Brackets from 1913-2020', page_icon=":money_with_wings:", layout="wide")

f  = 'cleaned_tax_1913_2020.csv'
df = pd.read_csv(f, index_col=0)
df = df[df['tax_type'] == 'Head']
st.write(df)

fig, ax = plt.subplots(1, figsize=(20,30))

norm = mpl.colors.Normalize(vmin=df['rate'].min(), vmax=df['rate'].max())


st.write(len(df['year'].unique()))

st.write(df)
cmap = sns.color_palette("rocket", as_cmap=True)
color = cmap(norm(df['rate']))

sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

p = ax.barh(y=df['year'], width=df['upper'], left=df['lower'], align='center', color=color)
ax.set_xscale('log')
# ax.set_xlim(0,5e5)
cbar = plt.colorbar(sm, ticks=range(0,101,10))
cbar.set_label('Tax Rate', rotation=270)
cbar.ax.set_ylim(0,100)

ax.set_yticks(df['year'].unique())
st.pyplot(fig)

