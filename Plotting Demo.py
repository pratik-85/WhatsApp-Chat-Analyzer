import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tempfile
import base64
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF
from tempfile import NamedTemporaryFile


st.title("📊 WhatsApp Chat Analyzer")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
    st.sidebar.write("###Rows and Columns: ",df.shape)
    if st.sidebar.checkbox("Top Statistics Table"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)
    figs=[]
      
    if st.sidebar.checkbox('Activity Map'):
        col1,col2 = st.columns(2)
        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            figs.append(fig)
        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            figs.append(fig)
    if st.sidebar.checkbox("Timeline"):
        col1,col2 = st.columns(2)
        
        with col1:
            st.title("Monthly Timeline")
            timeline = helper.monthly_timeline(df)
            fig,ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'],color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            figs.append(fig)
        with col2:
            st.title("Daily Timeline")
            daily_timeline = helper.daily_timeline(df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)  
            figs.append(fig)
    
    # if st.sidebar.checkbox("Most Common Word"):
    #     most_common_df = helper.most_common_words(df)
    #     fig,ax = plt.subplots()
    #     ax.barh(most_common_df[0],most_common_df[1])
    #     plt.xticks(rotation='vertical')
    #     st.title('Most commmon words')
    #     st.pyplot(fig) 
    #     figs.append(fig)
           
                
    if st.sidebar.checkbox("Emoji Analysis"):
        emoji_df=helper.emoji_helper(df)
        st.title("Emoji Analysis")
        col1,col2=st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.barh(emoji_df[0],emoji_df[1])
            st.pyplot(fig) 
            figs.append(fig)  
        
        # if emoji_df.shape[0] > 0:
        #     col1,col2 = st.columns(2)
        #     with col1:
        #         st.dataframe(emoji_df)
        #     with col2:
        #         fig,ax = plt.subplots()
        #         ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
        #         st.pyplot(fig)  
    if st.sidebar.checkbox("WordCloud"):
        st.title(":blue[Wordcloud]")
        df_wc = helper.create_wordcloud(df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc,interpolation='bilinear')
        st.pyplot(fig)
        figs.append(fig)
    
    if st.sidebar.checkbox("Weekly Activity Map"):
        st.title(":blue[Weekly Activity Map]")
        user_heatmap = helper.activity_heatmap(df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
        figs.append(fig)
                
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

export_as_pdf = st.button("Export Report")

if export_as_pdf:
    pdf = FPDF()
    for fig in figs:
        pdf.add_page()
        with NamedTemporaryFile(delete=False, suffix=".png") as tempfile:
            fig.savefig(tempfile.name)
            pdf.image(tempfile.name, 10, 10, 200, 100)
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "testfile")
    st.markdown(html, unsafe_allow_html=True)





        
    