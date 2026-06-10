import pandas as pd

from graph_vertical_percentage_bars import render_vertical_percentage_bar_graph


def render_problems_graph(
    general_df: pd.DataFrame,
    title: str = "Problems and guarantee",
    height: int = 300,
) -> None:
    problem_columns = [
        "1st year",
        "1st month",
        "Covered",
    ]

    render_vertical_percentage_bar_graph(
        general_df,
        problem_columns,
        title=title,
        height=height,
    )
