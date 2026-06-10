import streamlit as st

from dashboard_tab import render_dashboard_tab
from recommendation_tab import render_recommendation_tab
from research_tab import render_research_tab
from use_case_tab import render_use_case_tab


st.set_page_config(page_title="AI assisted used car purchasing", layout="wide")

st.title("AI assisted used car purchasing")

tab1, tab2, tab3, tab4 = st.tabs(["Use Case", "Dashboard", "Research", "Recommendation"])

with tab1:
    render_use_case_tab()

with tab2:
    render_dashboard_tab()

with tab3:
    render_research_tab()

with tab4:
    render_recommendation_tab()
