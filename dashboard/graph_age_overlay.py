import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


def render_age_overlay_graph(cars_df: pd.DataFrame, title: str = "Age distribution and cumulative share") -> None:
    st.subheader(title)

    age_counts_full = (
        cars_df["age"]
        .dropna()
        .astype(int)
        .value_counts()
        .sort_index()
    )

    if age_counts_full.empty:
        st.info("No age data available.")
        return

    cumulative_full = age_counts_full.cumsum() / age_counts_full.sum()
    age_counts = age_counts_full.loc[age_counts_full.index <= 10]
    cumulative_share = cumulative_full.loc[age_counts.index].tolist()
    ages = age_counts.index.tolist()
    counts = age_counts.tolist()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=ages,
            y=counts,
            name="Age distribution",
            marker=dict(color="rgba(31, 119, 180, 0.65)"),
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=ages,
            y=cumulative_share,
            name="Cumulative share",
            mode="lines+markers",
            line=dict(color="#d62728", width=3),
            marker=dict(size=7),
        ),
        secondary_y=True,
    )

    fig.update_layout(
        height=380,
        xaxis_title="",
        yaxis_title="Count",
        legend_title_text="",
        bargap=0.15,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.90,
            bgcolor="rgba(255, 255, 255, 0.6)",
        ),
    )
    fig.update_yaxes(title_text="Count", secondary_y=False)
    fig.update_yaxes(title_text="Cumulative share", tickformat=".0%", range=[0, 1], secondary_y=True)

    st.plotly_chart(fig, width="stretch")
