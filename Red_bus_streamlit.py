# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt

import time

def bus_details(bus_type, fare_min_value,fare_max_value,bus_rating,seat_avail):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS",auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        
        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"


        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min_value} AND {fare_max_value}
            AND Route_name = "{route}"
            AND {bus_type_condition} AND Start_time>='{TIME}' AND
            Ratings >={bus_rating} AND Seats_Available >= {seat_avail}
            ORDER BY Price and Start_time DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    
# kerala bus
lists_k=[]
df_k=pd.read_csv("Kerala route.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("Andhra route.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telangana bus
lists_T=[]
df_T=pd.read_csv("Telangana route.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Punjab bus
lists_p=[]
df_P=pd.read_csv("Punjab route.csv")
for i,r in df_P.iterrows():
    lists_p.append(r["Route_name"])

#Rajasthan bus
lists_R=[]
df_R=pd.read_csv("Rajasthan route.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# Bihar bus 
lists_B=[]
df_B=pd.read_csv("Bihar route.csv")
for i,r in df_B.iterrows():
    lists_B.append(r["Route_name"])

# HP bus
lists_HP=[]
df_HP=pd.read_csv("Himachal Pradesh route.csv")
for i,r in df_HP.iterrows():
    lists_HP.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("Assam route.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("Uttar Pradesh route.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("West Bengal route.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(page_title="redBus",layout="wide")
slt.title(":red[Welcome to the official site of redBus!:bus:]")


state = slt.selectbox("Lists of States", ["Kerala", "Andhra Pradesh", "Telangana", "Punjab", "Rajasthan",
                                       "Bihar", "Himachal Pradesh", "Assam", "Uttar Pradesh", "West Bengal"])      
col1,col2,col3,col4=slt.columns(4)
with col1:
    select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
with col2:
    input_min_fare = slt.number_input("Enter minimum bus fare range",min_value=None,value='min',placeholder="Type a number...")
    input_max_fare = slt.number_input("Enter maximum bus fare range",min_value=None,value='min',placeholder="Type a number...")
with col3:
    select_rating = slt.slider("Choose minimum bus rating",min_value=0.0,max_value=5.0,value=2.0,step=0.5)
with col4:
    select_seats_avail=slt.selectbox("No of seats required",[1,2,3,4,5,6,7,8,9,10])
TIME=slt.time_input("select the time")


if state == "Kerala":
    route = slt.selectbox("List of routes",lists_k)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Andhra Pradesh":
    route = slt.selectbox("List of routes",lists_A)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Telangana":
    route = slt.selectbox("List of routes",lists_T)
    df_result = bus_details(select_type,input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Punjab":
    route = slt.selectbox("List of routes",lists_p)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Rajasthan":
    route = slt.selectbox("List of routes",lists_R)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Bihar":
    route = slt.selectbox("List of routes",lists_B)
    df_result = bus_details(select_type,input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Himachal Pradesh":
    route = slt.selectbox("List of routes",lists_HP)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Assam":
    route = slt.selectbox("List of routes",lists_AS)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "Uttar Pradesh":
    route = slt.selectbox("List of routes",lists_UP)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)

if state == "West Bengal":
    route = slt.selectbox("List of routes",lists_WB)
    df_result = bus_details(select_type, input_min_fare,input_max_fare,select_rating,select_seats_avail)
    slt.dataframe(df_result)


    


