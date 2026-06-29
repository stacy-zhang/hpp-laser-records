import re
from html import escape

import streamlit as st
import pandas as pd

df = pd.read_csv("laser_systems.csv")

# Renders the references column so that values which are URLs become
# clickable links. Non-URL values (e.g. file names) are shown as plain text.
column_config = {
    "references": st.column_config.LinkColumn(
        "references",
        display_text=r"https?://(?:www\.)?([^/]+).*",
        width="large",
    )
}

search_query = st.text_input("Search for a laser system:")
if search_query: # filters if search query is not empty
    filtered_df = df[df['name'].str.contains(search_query, case=False, na=False)]
    st.dataframe(filtered_df, column_config=column_config) # displays the filtered dataframe
else: # query empty
    st.dataframe(df, column_config=column_config) # displays entire dataframe