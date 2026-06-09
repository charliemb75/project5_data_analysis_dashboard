import pandas as pd
import plotly.express as px
import streamlit as st


def render_customer_perspective_graph(
    general_df: pd.DataFrame,
    columns: list[str],
    title: str = "The customer perspective",
    height: int = 350,
) -> None:
    st.subheader(title)

    chart_df = (
        general_df[list(columns)]
        .melt(var_name="category", value_name="value")
        .assign(
            value=lambda df: pd.to_numeric(
                df["value"].astype(str).str.replace(",", ".", regex=False)
            )
        )
    )

    fig = px.bar(
        chart_df,
        x="category",
        y="value",
        color="category",
        text="value",
        labels={},
    )

    fig.update_traces(
        texttemplate="%{y:.0%}",
        textposition="outside",
        insidetextanchor="middle",
    )
    fig.update_layout(
        showlegend=False,
        height=height,
        yaxis_range=[0, 1],
        yaxis_tickformat=".0%",
        xaxis_title="",
        yaxis_title="",
        xaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_showgrid=False,
        yaxis_zeroline=False,
    )

    st.plotly_chart(fig, width="stretch")
