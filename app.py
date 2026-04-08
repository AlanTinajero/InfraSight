import streamlit as st
import pandas as pd
import time

from scanner import scan_network
from utils import get_vendor
from sniffer import sniff_traffic
from database import save_data, load_data
from alerts import detectar_anomalias

st.set_page_config(page_title="InfraSight", layout="wide")

# 🎯 UI estilo negro + verde
st.markdown("""
<style>
body { background-color: black; color: #39FF14; }
.stApp { background-color: black; }
h1,h2,h3 { color:#39FF14; }
</style>
""", unsafe_allow_html=True)

st.title("InfraSight")
st.markdown("Advanced Network Intelligence System")

st.markdown("""
STATUS: ACTIVE  
MODE: REAL-TIME MONITORING  
SECURITY LEVEL: MAXIMUM  
""")

ip_range = st.text_input("NETWORK RANGE", "192.168.100.0/24")

# 🔍 ESCANEO
def run_scan():
    devices = scan_network(ip_range)

    data = []

    for d in devices:
        vendor = get_vendor(d["mac"])

        data.append({
            "IP": d["ip"],
            "MAC": d["mac"],
            "VENDOR": vendor
        })

    return pd.DataFrame(data)

# 🚨 ALERTAS
def detectar_intrusos(df):
    return df[df["VENDOR"] == "Unknown"]

# ▶️ SCAN
if st.button("INITIATE SCAN"):

    st.write("Scanning network...")

    df = run_scan()

    st.subheader("DEVICES")
    st.dataframe(df)

    save_data(df)

    hist = load_data()

    alertas = detectar_anomalias(df, hist)

    st.subheader("THREAT ANALYSIS")

    if alertas:
        for a in alertas:
            st.error(a)
    else:
        st.success("NETWORK SECURE")

# 📡 TRAFFIC
if st.button("START TRAFFIC ANALYSIS"):

    st.write("Capturing traffic...")

    packets = sniff_traffic()

    df_packets = pd.DataFrame(packets)

    st.subheader("LIVE TRAFFIC")
    st.dataframe(df_packets)
