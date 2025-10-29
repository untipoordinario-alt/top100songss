import streamlit as st
import pandas as pd
from pymongo import MongoClient

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Datasheet con MongoDB Atlas", layout="wide")

st.title("📊 Datasheet conectado a MongoDB Atlas")

# --- CONEXIÓN A MONGODB ---
try:
    uri = st.secrets["mongodb"]["uri"]  # Se lee desde secrets.toml o Render env
    client = MongoClient(uri)
    db = client["miDB"]                 # Cambia por el nombre de tu base
    collection = db["miColeccion"]      # Cambia por el nombre de tu colección

    # --- OBTENER DATOS ---
    data = list(collection.find())
    if data:
        df = pd.DataFrame(data)
        st.success(f"Conectado correctamente ✅ — {len(df)} registros encontrados")
        st.dataframe(df)
    else:
        st.warning("No se encontraron documentos en la colección.")

except Exception as e:
    st.error(f"Error al conectar con MongoDB: {e}")
