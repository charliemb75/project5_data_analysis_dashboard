import pandas as pd
import plotly.express as px
import streamlit as st


def render_seller_graph(
    general_df: pd.DataFrame,
    title: str = "General market composition",
    height: int = 300,
) -> None:
    general_share_columns = [
        "Dealerships",
        "Private",
        "Auctions",
    ]

    general_share_df = (
        general_df[general_share_columns]
        .melt(var_name="category", value_name="value")
        .assign(
            group="Total",
            value=lambda df: pd.to_numeric(
                df["value"].astype(str).str.replace(",", ".", regex=False)
            )
        )
    )

    fig = px.bar(
        general_share_df,
        x="value",
        y="group",
        color="category",
        text="value",
        labels={},
    )

    fig.update_traces(
        texttemplate="%{x:.0%}",
        textposition="inside",
        insidetextanchor="middle",
    )
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center", y=0.98, yanchor="top"),
        showlegend=True,
        barmode="stack",
        height=height,
        margin=dict(l=0, r=0, t=55, b=10),
        xaxis_range=[0, 1],
        xaxis_tickformat=".0%",
        xaxis_title="",
        yaxis_title="",
        xaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_showgrid=False,
        yaxis_zeroline=False,
        legend_title_text="",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.2,
            xanchor="center",
            x=0.5,
        ),
    )

    st.plotly_chart(fig, width="stretch")
