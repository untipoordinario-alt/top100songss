import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.set_page_config(page_title="Datasheet con MongoDB Atlas", layout="wide")

st.title("📊 Datasheet conectado a MongoDB Atlas")

try:
    uri = st.secrets["mongodb"]["uri"]
    client = MongoClient(uri)
    db = client["miDB"]
    collection = db["miColeccion"]

    data = list(collection.find())
    if data:
        df = pd.DataFrame(data)
        st.success(f"Conectado correctamente ✅ — {len(df)} registros encontrados")
        st.dataframe(df)
    else:
        st.warning("No se encontraron documentos en la colección.")

except Exception as e:
    st.error(f"Error al conectar con MongoDB: {e}")
