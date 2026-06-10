import pandas as pd
import streamlit as st


def render_costs_text(general_df: pd.DataFrame) -> None:
    avg_cost_2014 = general_df["cost_14"].iloc[0]
    avg_cost_2026 = general_df["cost_26"].iloc[0]

    st.subheader("Average cost of a claim")
    st.markdown(
        f"""
        **Cost in 2014:** {avg_cost_2014} &euro;

        **Adjusted with inflation:** {avg_cost_2026} &euro; (+30% 2014-2026)
        """,
    )
