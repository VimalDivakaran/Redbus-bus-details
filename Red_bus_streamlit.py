# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
import time

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

#Punja bus
lists_p=[]
df_P=pd.read_csv("Punjab route.csv")
for i,r in df_P.iterrows():
    lists_p.append(r["Route_name"])

#Rajastan bus
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


S = slt.selectbox("Lists of States", ["Kerala", "Andhra Pradesh", "Telangana", "Punjab", "Rajasthan",
                                       "Bihar", "Himachal Pradesh", "Assam", "Uttar Pradesh", "West Bengal"])
        
col1,col2=slt.columns(2)
with col1:
    select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
with col2:
    select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
TIME=slt.time_input("select the time")

# Kerala bus fare filtering
if S == "Kerala":
    K = slt.selectbox("List of routes",lists_k)

    def type_and_fare(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{K}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare(select_type, select_fare)
    slt.dataframe(df_result)

# Andhra Pradesh bus fare filtering
if S=="Andhra Pradesh":
    A=slt.selectbox("list of routes",lists_A)

    def type_and_fare_A(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{A}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_A(select_type, select_fare)
    slt.dataframe(df_result)
    

# Telangana bus fare filtering
if S=="Telangana":
    T=slt.selectbox("list of routes",lists_T)

    def type_and_fare_T(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{T}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_T(select_type, select_fare)
    slt.dataframe(df_result)

# Punja bus fare filtering
if S=="Punjab":
    P=slt.selectbox("list of routes",lists_p)

    def type_and_fare_G(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{P}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_G(select_type, select_fare)
    slt.dataframe(df_result)

# Rajastan bus fare filtering
if S=="Rajasthan":
    R=slt.selectbox("list of routes",lists_R)

    def type_and_fare_R(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{R}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_R(select_type, select_fare)
    slt.dataframe(df_result)
    

# Bihar bus fare filtering       
if S=="Bihar":
    B=slt.selectbox("list of rotes",lists_B)

    def type_and_fare_B(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{B}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_B(select_type, select_fare)
    slt.dataframe(df_result)

# HP bus fare filtering
if S=="Himachal Pradesh":
    HP=slt.selectbox("list of routes",lists_HP)

    def type_and_fare_HP(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{HP}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_HP(select_type, select_fare)
    slt.dataframe(df_result)


# Assam bus fare filtering
if S=="Assam":
    AS=slt.selectbox("list of routes",lists_AS)

    def type_and_fare_AS(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{AS}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_AS(select_type, select_fare)
    slt.dataframe(df_result)

# Uttar Pradesh bus fare filtering
if S=="Uttar Pradesh":
    UP=slt.selectbox("list of routes",lists_UP)

    def type_and_fare_UP(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{UP}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
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

    df_result = type_and_fare_UP(select_type, select_fare)
    slt.dataframe(df_result)

# West Bengal bus fare filtering
if S=="West Bengal":
    WB=slt.selectbox("list of routes",lists_WB)

    def type_and_fare_WB(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="lamiv@1998", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{WB}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
            ORDER BY Price and Start_time  DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    df_result = type_and_fare_WB(select_type, select_fare)
    slt.dataframe(df_result)
