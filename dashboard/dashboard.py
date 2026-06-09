import streamlit as st

from import_data import load_data
from graph_depreciation import render_depreciation_graph
from graph_age_overlay import render_age_overlay_graph
from graph_customer_persp import render_customer_perspective_graph
from graph_problems import render_problems_graph
from graph_sales import render_sales_graph
from graph_sellers import render_seller_graph

st.set_page_config(page_title="AI assisted used car purchasing", layout="wide")

cars_df, general_df, sales_df, depreciation_df = load_data()

st.title("AI assisted used car purchasing")

sales_col, practices_col = st.columns([2, 1])
with sales_col:
    render_sales_graph(sales_df)
with practices_col:
    render_customer_perspective_graph(
        general_df,
        ["knowledge_cars", "knowledge_trading", "unfair_practices"],
        "The customer's perspective",
        height=350,
    )

market_col, problems_col, costs_col = st.columns(3, vertical_alignment="center")
with market_col:
    render_seller_graph(general_df)
with problems_col:
    render_problems_graph(general_df)
with costs_col:
    avg_cost_2014 = general_df["cost_14"].iloc[0]
    avg_cost_2026 = general_df["cost_26"].iloc[0]
    st.subheader("Average cost of a claim")
    st.markdown(
        f"""
        **Cost in 2014:** {avg_cost_2014} &euro;  
        **Adjusted with inflation:** {avg_cost_2026} &euro; (+30% 2014-2026)
        """,
    )

age_col, depreciation_col = st.columns(2)

with age_col:
    render_age_overlay_graph(cars_df)

with depreciation_col:
    render_depreciation_graph(depreciation_df)
