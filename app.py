import streamlit as st
import requests
import datetime

st.markdown('''# Taxi
            ''')

st.markdown('''### User input
            Please enter your data.
            ''')

d = st.date_input("Pickup date", datetime.date(2013, 7, 6))
t = st.time_input('Pickup time', datetime.time(17, 18))
timestamp_string = datetime.datetime.combine(d, t).strftime('%Y-%m-%d %H:%M:%S')

pick_lat = st.number_input('Pick-up lat', 40.783282)
pick_lon = st.number_input('Pick-up lon', -73.950655)
drop_lat = st.number_input('Drop-off lat', 40.769802)
drop_lon = st.number_input('Drop-off lon', -73.984365)

p_count = st.slider('Select a modulus', 1, 5, 1)



##

url_ = 'https://taxifare.lewagon.ai/predict'

params_ = {'pickup_datetime': timestamp_string,
           'pickup_longitude': pick_lon,
           'pickup_latitude': pick_lat,
           'dropoff_longitude': drop_lon,
           'dropoff_latitude': drop_lat,
           'passenger_count': p_count }

# 3. Let's call our API using the `requests` package...
response = requests.get(url=url_, params=params_)
print(response)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
r = response.json()
print(r)

## Finally, we can display the prediction to the user
st.markdown('''### Taxi fare prediction
            Please enter your data.
            ''')
st.text(f"The fare prediction is: {r['fare']} $")
