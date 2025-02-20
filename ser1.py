import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2= st.columns([0.5, 1])



with col1:
    st.title("SER")
    st.subheader("Quantity: 22")
    st.subheader("Size: 6 ft")
    st.link_button(label="Excel",
                   # url="https://1drv.ms/x/c/2f5d6a56f202642b/EQJ58CO4rZpBvep8a6Ru86oBGDugB_c1yW8rz48weAJtrA?e=km9iVn")
                     # url="https://1drv.ms/x/c/8de00afca386d6d5/EW1g77HDZydJic0Vet5QXaYB0kRlqipf75t6WhQ9VdxRfA?e=FutMWU")
                     url="https://onedrive.live.com/personal/8de00afca386d6d5/_layouts/15/doc.aspx?resid=b1ef606d-67c3-4927-89cd-157ade505da6&cid=8de00afca386d6d5&ct=1740085175166&wdOrigin=OFFICECOM-WEB.START.EDGEWORTH&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=db424c9f-d3c3-4105-baac-667541cc50cf")
        
    st.link_button(label="ser1",
                  url="https://excel.cloud.microsoft/open/onedrive/?docId=8DE00AFCA386D6D5%21sae9a56bb84f0413c975a7d6396cffd60&driveId=8DE00AFCA386D6D5")
with col2:
    st.image("1.jpg", width=300)
