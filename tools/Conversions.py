import re

import streamlit as st
from mgrs import MGRS


# Fonction de conversion DMS -> DD
def dms_to_decimal(dms: str) -> float:
    if dms is None:
        raise ValueError("Veuillez saisir une coordonnée DMS.")

    dms = dms.strip().upper().replace(" ", "")
    if not dms:
        raise ValueError("Veuillez saisir une coordonnée DMS.")

    direction = dms[-1]
    if direction not in ["N", "S", "E", "W"]:
        raise ValueError("Le format DMS doit se terminer par N, S, E ou W.")

    value = dms[:-1]
    if "°" not in value:
        raise ValueError("Le format DMS doit contenir des degrés (°).")

    match = re.fullmatch(
        r"(?P<degrees>\d+(?:[.,]\d+)?)°\s*(?:(?P<minutes>\d+(?:[.,]\d+)?)\s*['’′]" \
        r"\s*(?:(?P<seconds>\d+(?:[.,]\d+)?)\s*(?:\"|\"\"|”|″)?)?)?",
        value,
    )
    if match is None:
        raise ValueError(
            "Format DMS invalide. Exemple attendu : 48°51'29\"N ou 2°17'40\"E"
        )

    degrees = float(match.group("degrees"))
    minutes = float(match.group("minutes") or 0.0)
    seconds = float(match.group("seconds") or 0.0)

    if not 0 <= minutes < 60:
        raise ValueError("Les minutes doivent être comprises entre 0 et 59.")
    if not 0 <= seconds < 60:
        raise ValueError("Les secondes doivent être comprises entre 0 et 59.")

    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ["S", "W"]:
        decimal *= -1
    return decimal


def decimal_to_mgrs(lat_decimal, lon_decimal):
    m = MGRS()
    mgrs_coord = m.toMGRS(lat_decimal, lon_decimal)
    return mgrs_coord