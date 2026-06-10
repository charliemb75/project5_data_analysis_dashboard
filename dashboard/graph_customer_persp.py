import pandas as pd

from graph_vertical_percentage_bars import render_vertical_percentage_bar_graph


def render_customer_perspective_graph(
    general_df: pd.DataFrame,
    columns: list[str],
    title: str = "The customer's perspective",
    height: int = 300,
) -> None:
    render_vertical_percentage_bar_graph(
        general_df,
        columns,
        title=title,
        height=height,
    )
