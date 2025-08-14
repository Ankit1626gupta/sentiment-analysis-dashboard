import streamlit as st
import batch_analyzer as ba
import pandas as pd
import matplotlib.pyplot as plt
import db
import streamlit as st
st.title("Welcome To Tweet Analyzer 🐦")
query=st.text_input("Topic")
count=st.number_input("Number Of Tweets",min_value=1,step=1)
if st.button(" Run "):
    if count<10:
        st.warning("⚠️ Please Enter At Least 10 tweets")
    elif query.strip()=="":
        st.error("❌ Enter The Query ")
    else:
        ba.analyze_and_store(query,count)
        st.success("✅ Analysis Done")
        
if st.button("Analyzed table"):
    current_table=db.display(count)
    cm=pd.DataFrame(current_table, columns=['TEXT', 'TIMESTAMP', 'SENTIMENT'])
    st.dataframe(cm)
if st.button("Chart"):
    chart=db.display(count)
    df = pd.DataFrame(chart, columns=["TEXT","TIMESTAMP", "SENTIMENT"])
    s_c=df['SENTIMENT'].value_counts()
    fig, ax=plt.subplots()
    colors=["gray","green","red"]
    ax.pie(s_c, labels=s_c.index, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
st.subheader("To Get All Data Till Now")
if st.button("Get"):
    pre_table=db.table()
    cd=pd.DataFrame(pre_table, columns=['TEXT','TIMESTAMP', 'SENTIMENT'])
    st.dataframe(cd)
    df=db.get()
    st.subheader("Pie Chart Of Whole Data Till Now")
    sentiment_counts=df['SENTIMENT'].value_counts()
    fig, ax =plt.subplots()
    colors=["green","red","gray"]
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
