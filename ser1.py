import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, col3= st.columns([0.3, 0.5, 1])

with col1:
    st.title("SER")
    st.subheader("Quantity: 22")
    st.subheader("Size: 6 ft")
    st.link_button(label="Google sheets",
                   url="https://docs.google.com/spreadsheets/d/1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY/edit?usp=sharing")

with col2:
    st.image("1.jpg", width=300)

with col3:
    sheet_id = "1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY"
    # gid = "0"  
    # sheet_id = "1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY"
    gid = "687391187"

    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    df = pd.read_csv(csv_url, usecols=['Name', 'Quantity', 'Person', 'Event', 'Status', 'Total', 'Remaining'])

    st.dataframe(df, width= 515, hide_index=True, use_container_width=False)
    
    

    

