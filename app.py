import streamlit as st
import os
import pandas as pd
st.set_page_config(layout='wide')

def local_css():
    st.markdown("""
    <style>
    .stButton>button {
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# local_css()
directory = '/'
files = os.listdir(directory)

# Create a list to store file information
file_info = []

for file in files:
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        file_info.append([file, os.path.getsize(file_path)])


# Convert the list into a DataFrame
df = pd.DataFrame(file_info, columns=['File Name', 'Size (bytes)'])

col1, col2 = st.columns((1,3))


edited_df = st.data_editor(df, num_rows="dynamic")

# selected_file = st.sidebar.selectbox('Select a file', df['File Name'])

# # Display the content of the selected file
# if st.sidebar.button('Open'):
#     with open(os.path.join(directory, selected_file), 'r') as file:
#         st.text(file.read())
