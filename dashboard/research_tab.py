import streamlit as st
from pathlib import Path


def render_research_tab() -> None:
    research_path = Path(__file__).resolve().parent.parent / "research" / "research.md"
    st.markdown(research_path.read_text(encoding="utf-8"))
