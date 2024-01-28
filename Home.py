import streamlit as st
# import Plotting_Demo
st.set_page_config(
    page_title = "Home",
    # page_icon = "",
)

st.header("📶Welcome to WhatsApp Chat Analyzer📶")



st.markdown(
    """WhatsApp is a free cross-platform messaging service. It lets users of iPhone and Android smartphones and Mac and Windows PC call and exchange text, photo, audio and video messages with others across the globe for free, regardless of the recipient's device.
    """)
st.markdown("""WhatsApp Chat Analyzer web app creted using the Streamlit Library. This Streamlit Library is open source 
    library for machine learning and data science project. In this project we can calculate the number of messages send by the user , linked shared, media shared , emoji , etc.
    """)
st.markdown("""In this project , we use the various library like seaborn , streamlit , datetime , regex , matplotlib , 
    numpy , pandas etc. 
    """)

st.markdown("""👉 Steps for WhatsApp Chat Analyzer : -
    
    """)
st.markdown("""1) Upload the dataset""")
st.markdown("""2) Select which visualization you have to need""")
st.markdown("""3) After Showing visualization, click on Export Report that can create the Download file link & click it.""")
st.markdown("""4) Go to the Information Tab, fill the information that can shwo in Top Statistics Table and Click on Submit Button and it can show the Submitted Successfully.""")
st.markdown("""4) Go to the PDF UPLOADER Tab, upload the downloaded pdf and store into the tempDir.""")