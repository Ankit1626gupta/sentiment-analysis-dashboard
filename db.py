
import pandas as pd
import pymysql
import pandas as pd
def make_connection():
    mydb=pymysql.connect(host="localhost",user="root",password="ankit@16",database="sentiment_analysis")
    return mydb




def insert_data(text,sentiment):
    mydb=make_connection()
    cursor=mydb.cursor()
    qu="INSERT INTO feedback(TEXT,SENTIMENT) VALUES(%s,%s)"
    cursor.execute(qu,(text,sentiment))
    mydb.commit()

def display(count):
    mydb=make_connection()
    cursor=mydb.cursor()
    o="SELECT * FROM feedback ORDER BY TIMESTAMP DESC LIMIT %s"
    cursor.execute(o,(count,))
    rows = cursor.fetchall()
    return rows
def get():
    mydb=make_connection()
    cursor=mydb.cursor()
    cursor.execute("SELECT TEXT,SENTIMENT,TIMESTAMP FROM feedback ORDER BY TIMESTAMP")  
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['TEXT', 'SENTIMENT', 'TIMESTAMP'])
    return df
def table():
    mydb=make_connection()
    cursor=mydb.cursor()
    o="SELECT * FROM feedback"
    cursor.execute(o)
    rows = cursor.fetchall()
    return rows
def wil(query):
    mydb=make_connection()
    cursor=mydb.cursor()
    sql="SELECT * FROM feedback WHERE TEXT LIKE %s"
    param=('%'+query+'%',)
    cursor.execute(sql,param)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['TEXT', 'SENTIMENT', 'TIMESTAMP'])
    cursor.close()
    mydb.close()
    return rows



