import pandas as pd
import plotly.express as px
import streamlit as st


def render_seller_graph(general_df: pd.DataFrame) -> None:
    st.subheader("General market composition")

    general_share_columns = [
        "fraction_dealerships",
        "fraction_private",
        "fraction_auctions",
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
        showlegend=True,
        barmode="stack",
        height=350,
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
