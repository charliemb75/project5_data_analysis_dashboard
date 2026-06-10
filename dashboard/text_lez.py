from __future__ import annotations

import pandas as pd
import streamlit as st


def _as_number(value: object) -> float:
    if isinstance(value, str):
        return float(value.replace(",", "."))
    return float(value)


def render_lez_text(general_df: pd.DataFrame) -> None:
    currently_lez_millions = _as_number(general_df["currently_lez_millions"].iloc[0])
    currently_lez_fraction = _as_number(general_df["currently_lez_fraction"].iloc[0])
    urban_millions = _as_number(general_df["urban_millions"].iloc[0])
    urban_fraction = _as_number(general_df["urban_fraction"].iloc[0])

    st.markdown(
        f"""
        As of October 2024:
        
        **Living within a LEZ:** {currently_lez_millions:.1f} million ({currently_lez_fraction:.0%})

        **Living in urban areas:** {urban_millions:.1f} million ({urban_fraction:.0%})
        """
    )
