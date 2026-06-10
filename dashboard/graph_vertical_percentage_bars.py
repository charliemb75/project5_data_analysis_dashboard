import pandas as pd
import plotly.express as px
import streamlit as st


def render_vertical_percentage_bar_graph(
    df: pd.DataFrame,
    columns: list[str],
    title: str,
    height: int = 300,
) -> None:
    chart_df = (
        df[list(columns)]
        .melt(var_name="category", value_name="value")
        .assign(
            value=lambda data: pd.to_numeric(
                data["value"].astype(str).str.replace(",", ".", regex=False)
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
        title=dict(text=title, x=0.5, xanchor="center", y=0.98, yanchor="top"),
        showlegend=False,
        height=height,
        margin=dict(l=0, r=0, t=55, b=10),
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
