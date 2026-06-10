import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render_euro_timeline(
    euro_df: pd.DataFrame,
    title: str = "Emissions Milestones in the EU",
) -> None:
    chart_df = euro_df.head(8).copy()
    chart_df["date"] = pd.to_datetime(chart_df["date"], format="%d/%m/%Y")
    timeline_dates = chart_df["date"].tolist()
    boundaries = [
        pd.Timestamp("1990-01-01"),
        *timeline_dates,
        pd.Timestamp("2040-12-31"),
    ]
    lower_milestones = [
        {"label": "DE Petrol", "date": pd.Timestamp("1993-01-01"), "y": -0.15},
        {"label": "DE Diesel", "date": pd.Timestamp("2006-01-01"), "y": -0.15},
        {"label": "ES Petrol", "date": pd.Timestamp("2006-01-01"), "y": -0.22},
        {"label": "ES Diesel", "date": pd.Timestamp("2015-09-01"), "y": -0.15},
    ]
    current_date = pd.Timestamp.today().normalize()
    next_month_start = (current_date + pd.offsets.MonthBegin(1)).normalize()
    avg_age_years = float(str(euro_df.iloc[-1]["date"]).replace(",", "."))
    next_month_minus_age = next_month_start - pd.Timedelta(days=avg_age_years * 365.25)
    lower_milestones.extend(
        [
            {"label": "Today", "date": next_month_start, "y": -0.25},
            {
                "label": f"Average production date<br>Fleet age: {avg_age_years:.1f} years",
                "date": next_month_minus_age,
                "y": -0.25,
            },
        ]
    )

    fig = go.Figure()
    colors = [
        "#d73027",
        "#f46d43",
        "#fdae61",
        "#fee08b",
        "#d9ef8b",
        "#a6d96a",
        "#66bd63",
        "#1a9850",
    ]

    segment_starts = boundaries[:-1]
    segment_ends = boundaries[1:]
    segment_colors = [*colors, "#9ecae1"]

    for idx, (start, end) in enumerate(zip(segment_starts, segment_ends)):
        if idx < len(chart_df):
            fig.add_annotation(
                x=timeline_dates[idx],
                y=0.17,
                text=chart_df.iloc[idx]["milestone"],
                showarrow=False,
                yanchor="bottom",
                xanchor="center",
                font=dict(size=11, color="#222222"),
            )
        fig.add_shape(
            type="rect",
            x0=start,
            x1=end,
            y0=-0.1,
            y1=0.1,
            line=dict(width=0),
            fillcolor=segment_colors[idx],
            opacity=0.85,
        )

    fig.add_trace(
        go.Scatter(
            x=[pd.Timestamp("1990-01-01"), pd.Timestamp("2040-12-31")],
            y=[0, 0],
            mode="lines",
            line=dict(color="rgba(80, 80, 80, 0.75)", width=2),
            showlegend=False,
            hoverinfo="skip",
        )
    )

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center"),
        height=250,
        margin=dict(l=0, r=0, t=35, b=25),
        xaxis_title="",
        yaxis_title="",
        xaxis_range=[pd.Timestamp("1990-01-01"), pd.Timestamp("2040-12-31")],
        yaxis_range=[-0.48, 0.35],
        yaxis_visible=False,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_zeroline=False,
        showlegend=False,
    )

    for item in lower_milestones:
        fig.add_annotation(
            x=item["date"],
            y=item["y"],
            text=item["label"],
            showarrow=True,
            arrowhead=0,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor="rgba(80, 80, 80, 0.7)",
            ax=0,
            ay=25,
            yanchor="top",
            xanchor="center",
            align="center",
            font=dict(size=10, color="#222222"),
        )

    st.plotly_chart(fig, width="stretch")
