import pandas as pd
import plotly.express as px
import streamlit as st


def render_problems_graph(general_df: pd.DataFrame) -> None:
    st.subheader("Problems and guarantee")

    problem_columns = [
        "problems_1_year",
        "problems_1_month",
        "covered_guarantee",
    ]

    problem_df = (
        general_df[problem_columns]
        .melt(var_name="category", value_name="value")
        .assign(
            value=lambda df: pd.to_numeric(
                df["value"].astype(str).str.replace(",", ".", regex=False)
            )
        )
    )

    fig = px.bar(
        problem_df,
        x="category",
        y="value",
        color="category",
        text="value",
        labels={},
    )

    fig.update_traces(
        texttemplate="%{y:.0%}",
        textposition="outside",
    )

    fig.update_layout(
        showlegend=False,
        height=450,
        margin=dict(t=70),
        yaxis_range=[0, 1],
        yaxis_tickformat=".0%",
        yaxis_title="",
        yaxis_showgrid=False,
        yaxis_zeroline=False,
        xaxis_title="",
        xaxis_showgrid=False,
        xaxis_zeroline=False,
    )

    st.plotly_chart(fig, width="stretch")
