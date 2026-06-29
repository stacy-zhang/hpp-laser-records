import streamlit as st
import pandas as pd

df = pd.read_csv("laser_systems.csv")
search_query = st.text_input("Search for a laser system:")
if search_query: # filters if search query is not empty
    filtered_df = df[df['name'].str.contains(search_query, case=False, na=False)]
    st.write(filtered_df) # displays the filtered dataframe
else: # query empty
    st.write(df) # displays entire dataframe