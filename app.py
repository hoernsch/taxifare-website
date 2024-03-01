import streamlit as st
import requests

import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

d = st.date_input("Pickup date", datetime.date(2013, 7, 6))
t = st.time_input('Pickup time', datetime.time(17, 18))

pick_lat = st.number_input('Pick-up lat', 40.783282)
pick_lon = st.number_input('Pick-up lon', -73.950655)
drop_lat = st.number_input('Drop-off lat', 40.769802)
drop_lon = st.number_input('Drop-off lon', -73.984365)

p_count = st.slider('Select a modulus', 1, 5, 1)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



url_ = 'https://taxifare.lewagon.ai/predict'

#if url_ == 'https://taxifare.lewagon.ai/predict':
#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...

timestamp_string = datetime.datetime.combine(d, t).strftime('%Y-%m-%d %H:%M:%S')


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

## Finally, we can display the prediction to the user
st.text(f"The fare prediction is: {r['fare']} $")
