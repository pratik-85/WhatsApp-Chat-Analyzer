from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import string
import re
import emoji

extract = URLExtract()

def fetch_stats(df):    
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())
        
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
    
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages,len(words),num_media_messages,len(links)

# def remove_stop_words(message):
#     f = open('stop_hinglish.txt','r')
#     stop_words = f.read()
#     y = []
#     for word in message.lower().split():
#         if word not in stop_words:
#             y.append(word)
#     return " ".join(y)

# def remove_punctuation(message):
#     x = re.sub('[%s]'% re.escape(string.punctuation),'',message)
#     return x

def create_wordcloud(df):
    temp = df[df['user'] != 'group_notification']
    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != '<Media omitted>\n']
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def emoji_helper(df):
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df   

def monthly_timeline(df):
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline 

def daily_timeline(df):
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(df):
    return df['day_name'].value_counts()

def month_activity_map(df):
    return df['month'].value_counts()

def activity_heatmap(df):
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap