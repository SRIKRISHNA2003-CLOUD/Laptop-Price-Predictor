
import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")

# Brand
company = st.selectbox('Brand', df["Company"].unique())

# Type Of laptop
type = st.selectbox('Type', df["TypeName"].unique())

# RAM
ram = st.selectbox("Ram", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input(
    "Weight (kg)",
    min_value=0.5,
    max_value=5.0,
    step=0.1
)

# Touch Screen
touchscreen = st.selectbox("TouchScreen", ['NO', 'Yes'])

# IPS
ips = st.selectbox("IPS", ['NO', 'Yes'])

# Screen Size
screen_size = st.number_input(
    "Screen Size (inches)",
    min_value=10.0,
    max_value=18.0,
    step=0.1
)

# Resolution
resolution = st.selectbox(
    "Screen Resolution",
    [
        '1366×768',
        '1600×900',
        '1536×864',
        '1920×1080',
        '1920×1200',
        '2300×1440',
        '2560×1440',
        '2560×1600'
    ]
)

# CPU
cpu = st.selectbox('CPU', df["Cpu Brands"].unique())

# HDD
hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox("Gpu Brand", df["Gpu Brand"].unique())

# OS
os = st.selectbox("OS", df["Os"].unique())


if st.button("Predict Price"):

    # Convert TouchScreen to 0/1
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    # Convert IPS to 0/1
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    # Extract resolution
    X_res = int(resolution.split('×')[0])
    Y_res = int(resolution.split('×')[1])

    # Calculate PPI
    ppi = (((X_res ** 2) + (Y_res ** 2)) ** 0.5) / screen_size

    # Create input array
    query = np.array([
        company,
        type,
        ram,
        weight,
        touchscreen,
        ips,
        ppi,
        cpu,
        hdd,
        ssd,
        gpu,
        os
    ])

    query = query.reshape(1, 12)

    # Predict price
    prediction = np.round(np.exp(pipe.predict(query)[0]))

    st.title(f"Predicted Price for this configuration: ₹{prediction:,.0f}")

