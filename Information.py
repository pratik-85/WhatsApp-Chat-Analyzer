import streamlit as st
from pathlib import Path
import sqlite3

conn = sqlite3.connect('What_db.db',check_same_thread=False)
st.sidebar.header("📃 Information ")
cur = conn.cursor()
def form():
    st.header(f"Count of Message")
    st.markdown("Please fill the form")
    name = st.text_input(label="Name of User",type="default" )
    with st.form(key="Message_Information", clear_on_submit=True):
        total_message = st.number_input(label="Total Messages",min_value=0)
        total_words = st.number_input(label="Total Words",min_value=0)
        total_media = st.number_input(label="Media Shared",min_value=0)
        total_link = st.number_input(label="Link Shared",min_value=0) 
        submitted = st.form_submit_button(label="Submit")
        if submitted == True:
            addData(name,total_message,total_words,total_media,total_link)
                                      
def addData(a,b,c,d,e):
    cur.execute("""CREATE TABLE IF NOT EXISTS WHAT_DB(NAME_OF_USER VARCHAR(100),TOTAL_MESSAGE INT,TOTAL_WORDS INT, TOTAL_MEDIA INT, TOTAL_LINK INT);""")  
    cur.execute("INSERT INTO WHAT_DB VALUES (?,?,?,?,?)",(a,b,c,d,e))  
    conn.commit()
    conn.close()
    st.success("Successfully Submitted!!")       
form()  