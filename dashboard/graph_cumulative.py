from __future__ import annotations

import math

import pandas as pd
import plotly.express as px
import streamlit as st


def _render_cumulative_line(
    labels: list[str],
    cum_pct: list[float],
    title: str,
    height: int = 320,
) -> None:
    chart_df = pd.DataFrame({"label": labels, "cum_pct": cum_pct})

    fig = px.line(chart_df, x="label", y="cum_pct", markers=True)
    fig.update_traces(line=dict(width=3))
    fig.update_layout(
        height=height,
        xaxis_title="",
        yaxis_title="",
        yaxis_range=[0, 1],
        yaxis_tickformat=".0%",
        showlegend=False,
    )

    st.subheader(title)
    st.plotly_chart(fig, width="stretch")


def render_age_cumulative(cars_df: pd.DataFrame, title: str = "Age cumulative share") -> None:
    ages = (
        cars_df["age"]
        .dropna()
        .astype(int)
        .value_counts()
        .sort_index()
    )
    cum_pct = (ages.cumsum() / ages.sum()).tolist()
    labels = [str(age) for age in ages.index.tolist()]

    _render_cumulative_line(labels, cum_pct, title)


def render_mileage_cumulative(
    cars_df: pd.DataFrame,
    title: str = "Mileage cumulative share",
    step: int = 20_000,
) -> None:
    mileage = cars_df["mileage"].dropna()
    if mileage.empty:
        _render_cumulative_line([], [], title)
        return

    min_edge = math.floor(mileage.min() / step) * step
    max_edge = math.ceil(mileage.max() / step) * step
    if max_edge == min_edge:
        max_edge = min_edge + step

    edges = list(range(int(min_edge), int(max_edge) + step, step))
    bins = pd.cut(mileage, bins=edges, include_lowest=True, right=False)
    counts = bins.value_counts(sort=False)
    cum_pct = [0.0] + (counts.cumsum() / counts.sum()).tolist()
    labels = ["0k"] + [f"{int(interval.right / 1000):.0f}k" for interval in counts.index]

    _render_cumulative_line(labels, cum_pct, title)
