import streamlit as st

from graph_age_overlay import render_age_overlay_graph
from graph_customer_persp import render_customer_perspective_graph
from graph_depreciation import render_depreciation_graph
from graph_lez_map import render_lez_map
from graph_problems import render_problems_graph
from graph_sales import render_sales_graph
from graph_sellers import render_seller_graph
from graph_timeline import render_euro_timeline
from import_data import load_data
from text_costs import render_costs_text
from text_lez import render_lez_text


def render_dashboard_tab() -> None:
    cars_df, general_df, sales_df, depreciation_df, lez_df, euro_df = load_data()

    st.subheader("Historic Situation of the Used-Car Market")
    first_row_height = 380
    vertical_percentage_height = 300
    market_height = 300

    title_sales = "Market volume"
    title_perspective = "The customer's perspective"
    title_market = "General market composition"
    title_problems = "Problems and guarantee"
    title_depreciation = "Depreciation comparison"
    title_age = "Age distribution and cumulative share"
    title_lez = "Low Emission Zones in Europe"
    title_timeline = "Emissions Milestones in the EU"

    sales_col, practices_col = st.columns([2, 1])
    with sales_col:
        render_sales_graph(sales_df, title=title_sales, height=first_row_height)
    with practices_col:
        render_customer_perspective_graph(
            general_df,
            ["Know cars", "Know trading", "Unfair treatment"],
            title=title_perspective,
            height=first_row_height,
        )

    market_col, problems_col, costs_col = st.columns(3, vertical_alignment="center")
    with market_col:
        render_seller_graph(general_df, title=title_market, height=market_height)
    with problems_col:
        render_problems_graph(
            general_df,
            title=title_problems,
            height=vertical_percentage_height,
        )
    with costs_col:
        render_costs_text(general_df)

    st.subheader("Impact of the Emissions Regulations in Europe")

    render_euro_timeline(euro_df, title=title_timeline)

    lez_map_col, lez_text_col = st.columns([2, 1], vertical_alignment="center")
    with lez_map_col:
        render_lez_map(lez_df, title=title_lez)
    with lez_text_col:
        render_lez_text(general_df)

    st.subheader("Age Distribution and Depreciation")

    age_col, depreciation_col = st.columns(2)
    with age_col:
        render_age_overlay_graph(cars_df, title=title_age)
    with depreciation_col:
        render_depreciation_graph(depreciation_df, title=title_depreciation)
