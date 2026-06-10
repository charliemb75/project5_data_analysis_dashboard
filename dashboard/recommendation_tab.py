from pathlib import Path

import streamlit as st


def render_recommendation_tab() -> None:
    recommendation_path = (
        Path(__file__).resolve().parent.parent
        / "implementation"
        / "recommendation_implementation.md"
    )
    st.markdown(recommendation_path.read_text(encoding="utf-8"))
