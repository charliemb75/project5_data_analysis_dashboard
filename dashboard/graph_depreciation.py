import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render_depreciation_graph(depreciation_df: pd.DataFrame) -> None:
    st.subheader("Depreciation comparison")

    pair_styles = {
        "Autoexp": {"color": "#1f77b4"},
        "Motorway": {"color": "#ff7f0e"},
        "Carwow": {"color": "#2ca02c"},
    }
    series_styles = {
        "Autoexp 1": {"dash": "solid"},
        "Autoexp 2": {"dash": "dash"},
        "Motorway 1": {"dash": "solid"},
        "Motorway 2": {"dash": "dash"},
        "Carwow 1": {"dash": "solid"},
        "Carwow 2": {"dash": "dash"},
    }

    fig = go.Figure()
    x_values = depreciation_df["Year"]
    value_columns = [
        "Autoexp 1",
        "Autoexp 2",
        "Motorway 1",
        "Motorway 2",
        "Carwow 1",
        "Carwow 2",
    ]

    for column in value_columns:
        y_values = depreciation_df[column]
        if column.startswith("Autoexp"):
            color = pair_styles["Autoexp"]["color"]
        elif column.startswith("Motorway"):
            color = pair_styles["Motorway"]["color"]
        elif column.startswith("Carwow"):
            color = pair_styles["Carwow"]["color"]

        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                mode="lines",
                name=column,
                line=dict(
                    color=color,
                    dash=series_styles.get(column, {}).get("dash", "solid"),
                    width=3 if column.endswith("1") or column == "BLS" else 2,
                ),
            )
        )

    max_values = depreciation_df[value_columns].max(axis=1)
    min_values = depreciation_df[value_columns].min(axis=1)

    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=max_values,
            mode="lines",
            name="Maximum",
            line=dict(color="rgba(173, 216, 230, 0.0)", width=0),
            showlegend=False,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=min_values,
            mode="lines",
            name="Minimum",
            line=dict(color="rgba(173, 216, 230, 0.0)", width=0),
            fill="tonexty",
            fillcolor="rgba(173, 216, 230, 0.3)",
            showlegend=False,
        )
    )

    fig.update_layout(
        height=380,
        xaxis_title="Year",
        yaxis_title="",
        yaxis_range=[0, 105],
        yaxis_tickformat=".0f",
        legend_title_text="",
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
