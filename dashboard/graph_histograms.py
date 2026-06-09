import math

import pandas as pd
import plotly.express as px
import streamlit as st


def render_histogram(
    cars_df: pd.DataFrame,
    column: str,
    bins: int,
    title: str | None = None,
    height: int = 320,
) -> None:
    st.subheader(title or column.replace("_", " ").title())

    fig = px.histogram(cars_df, x=column, nbins=bins)
    fig.update_layout(
        height=height,
        xaxis_title="",
        yaxis_title="",
        bargap=0.05,
    )

    st.plotly_chart(fig, width="stretch")


def render_age_histogram(cars_df: pd.DataFrame, title: str = "Age distribution") -> None:
    age_min = cars_df["age"].min()
    age_max = cars_df["age"].max()
    age_bins = max(1, math.ceil(age_max - age_min) + 1)

    render_histogram(
        cars_df,
        column="age",
        bins=age_bins,
        title=title,
    )
