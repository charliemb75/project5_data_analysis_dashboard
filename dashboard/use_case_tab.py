from pathlib import Path

import streamlit as st


def render_use_case_tab() -> None:
    use_case_path = Path(__file__).resolve().parent.parent / "research" / "use_case.md"
    st.markdown(use_case_path.read_text(encoding="utf-8"))
