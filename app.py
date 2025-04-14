import streamlit as st
import pandas as pd
import pickle

with open("aqi.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌫️ Air Quality Index (AQI) Predictor")

st.markdown("Enter the pollutant levels below to predict the Air Quality Index.")

city = st.selectbox("Select City", [
    "Ahmedabad", "Aizawl", "Amaravati", "Amritsar", "Bengaluru", "Bhopal", "Brajrajnagar",
    "Chandigarh", "Chennai", "Coimbatore", "Delhi", "Ernakulam", "Gurugram", "Guwahati", 
    "Hyderabad", "Jaipur", "Jorapokhar", "Kochi", "Kolkata", "Lucknow", "Mumbai", "Nagpur", 
    "Patna", "Pune", "Shillong", "Talcher", "Thiruvananthapuram", "Visakhapatnam", "Vijayawada"
])

pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no = st.number_input("NO", min_value=0.0)
no2 = st.number_input("NO2", min_value=0.0)
nox = st.number_input("NOx", min_value=0.0)
nh3 = st.number_input("NH3", min_value=0.0)
co = st.number_input("CO", min_value=0.0)
so2 = st.number_input("SO2", min_value=0.0)
o3 = st.number_input("O3", min_value=0.0)
benzene = st.number_input("Benzene", min_value=0.0)
toluene = st.number_input("Toluene", min_value=0.0)
xylene = st.number_input("Xylene", min_value=0.0)

if st.button("Predict AQI"):
    input_data = pd.DataFrame({
        "City": [city],
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO": [no],
        "NO2": [no2],
        "NOx": [nox],
        "NH3": [nh3],
        "CO": [co],
        "SO2": [so2],
        "O3": [o3],
        "Benzene": [benzene],
        "Toluene": [toluene],
        "Xylene": [xylene]
    })

    input_data = pd.get_dummies(input_data)
    model_columns = model.feature_names_in_
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_data)[0]
    st.success(f"🌍 Predicted AQI: **{round(prediction, 2)}**")
