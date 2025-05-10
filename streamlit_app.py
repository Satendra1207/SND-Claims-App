import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title='SSC & Atta Damage Submission Details',
    page_icon='📊'
)

st.title(":rainbow[SSC & Atta Damage Submission Details May to Feb'25]")
st.subheader(':red[You can find your WD_Claims below]', divider='rainbow')

# Load Excel data
file_path = r"C:\Users\s172417\OneDrive - Cargill Inc\desktop\App Data\SSC & Atta Damage Submission Details May to Feb'25.xlsx"
data = pd.read_excel(file_path)

# Clean column names
data.columns = data.columns.str.strip()
data['WD Code'] = data['WD Code'].astype(str).str.strip()

# WD Code input
WD_Code = st.text_input("Please Enter Your WD Code")

if 'show_form' not in st.session_state:
    st.session_state['show_form'] = False

if WD_Code:
    WD_Code = WD_Code.strip()
    filtered_data = data[data['WD Code'] == WD_Code]

    if not filtered_data.empty:
        st.success("✅ Data Found Successfully")

        tab1, tab2, tab3 = st.tabs(["All","OIL", "ATTA"])

        with tab2:
            oil = filtered_data[filtered_data['Product Category'].str.strip() == "OIL"]
            if not oil.empty:
                oil=oil.reset_index(drop=True)
                st.dataframe(oil,hide_index=True)
            else:
                st.warning("⚠️ No data found under 'OIL'")

        with tab3:
            atta = filtered_data[filtered_data['Product Category'].str.strip() == "ATTA"]
            if not atta.empty:
                atta=atta.reset_index(drop=True)
                st.dataframe(atta,hide_index=True)

        with tab1:
            filtered_data=filtered_data.reset_index(drop=True)
            st.dataframe(filtered_data,hide_index=True)

    else:
        st.warning("⚠️ No data found for this WD Code")
