import os
import streamlit as st
from pymongo import MongoClient

# Buscar el URI en secrets o variables de entorno
MONGO_URI = st.secrets.get("MONGO_URI", os.getenv("MONGO_URI"))

if not MONGO_URI:
    st.error("❌ No se encontró la variable MONGO_URI. Configúrala en Render → Environment.")
else:
    try:
        client = MongoClient(MONGO_URI)
        db = client["tu_basededatos"]
        st.success("✅ Conectado a MongoDB Atlas correctamente.")
    except Exception as e:
        st.error(f"Error al conectar con MongoDB: {e}")
