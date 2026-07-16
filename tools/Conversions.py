import streamlit as st
from mgrs import MGRS

# Fonction de conversion DMS -> DD
def dms_to_decimal(dms: str) -> float:
    dms = dms.strip().upper().replace(' ', '')
    if not dms:
        raise ValueError("Veuillez saisir une coordonnée DMS.")
    if dms[-1] not in ['N', 'S', 'E', 'W']:
        raise ValueError("Le format DMS doit se terminer par N, S, E ou W.")

    direction = dms[-1]
    value = dms[:-1]

    if '°' not in value:
        raise ValueError("Le format DMS doit contenir des degrés (°).")

    degrees_part, rest = value.split('°', 1)
    degrees = float(degrees_part) if degrees_part else 0.0
    minutes = 0.0
    seconds = 0.0

    if "'" in rest:
        minutes_part, rest = rest.split("'", 1)
        minutes = float(minutes_part) if minutes_part else 0.0
    if '"' in rest:
        seconds_part = rest.split('"', 1)[0]
        seconds = float(seconds_part) if seconds_part else 0.0

    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal


def decimal_to_mgrs(lat_decimal, lon_decimal):
    m = MGRS()
    mgrs_coord = m.toMGRS(lat_decimal, lon_decimal)
    return mgrs_coord