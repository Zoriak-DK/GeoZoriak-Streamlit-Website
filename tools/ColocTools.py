import streamlit as st
import pandas as pd
import numpy as np

def colocalisation(df: pd.DataFrame, type_coloc: str) -> pd.DataFrame:
    df_init = df
    if type_coloc == "spatial":
        df_init = df.copy()
    elif type_coloc == "spatio-temporel":
        df_init = df.copy()
