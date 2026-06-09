import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render_sales_graph(sales_df: pd.DataFrame) -> None:
    st.subheader("Market volume")

    chart_df = sales_df[["Used", "Total"]].copy()
    chart_df["Used"] = pd.to_numeric(
        chart_df["Used"].astype(str).str.replace(",", ".", regex=False)
    )
    chart_df["Total"] = pd.to_numeric(
        chart_df["Total"].astype(str).str.replace(",", ".", regex=False)
    )

    fig = go.Figure()
    fig.add_bar(
        x=chart_df["Total"],
        y=chart_df.index,
        orientation="h",
        name="Total",
        text=chart_df["Total"],
        texttemplate="%{x:.2f}",
        textposition="outside",
    )
    fig.add_bar(
        x=chart_df["Used"],
        y=chart_df.index,
        orientation="h",
        name="Used",
        text=chart_df["Used"],
        texttemplate="%{x:.2f}",
        textposition="outside",
    )

    fig.update_layout(
        height=350,
        xaxis_title="",
        yaxis_title="",
        xaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_showgrid=False,
        yaxis_zeroline=False,
        legend_title_text="",
        barmode="group",
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="right",
            x=0.98,
            bgcolor="rgba(255, 255, 255, 0.6)",
        ),
    )

    st.plotly_chart(fig, width="stretch")
