import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect

#Define a sql to fetch data from CARS table from postgre sql hosted on heroku
sql = 'Select * from cars c;'
#call postgreconnect.runquery function and pass sql.this function will return data from CARS table
#convert returned data into a dataframe
record = pd.DataFrame(postgreconnect.runquery(sql))
#Add column header - 9 columns
record.column=['Name','Miles_Per_Gallon','Cylinders','Displacement','Horsespeed','Weight_In_Lbs','Acceleration','Year','Origin']
#Add title to streamlit app
st.title('Cars data - Sourced from Heroku')
#The contents were printed on a table
st.table(record)
