import pandas as pd
import plotly.express as px
import streamlit as st


def render_lez_map(
    lez_df: pd.DataFrame,
    title: str = "Low Emission Zones in Europe",
) -> None:
    chart_df = lez_df.copy()
    chart_df["population_LEZs"] = pd.to_numeric(
        chart_df["population_LEZs"].astype(str).str.replace(",", ".", regex=False)
    )

    fig = px.choropleth(
        chart_df,
        locations="country",
        color="population_LEZs",
        color_continuous_scale="Blues",
        scope="world",
        labels={"population_LEZs": "Population in LEZs"},
    )

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor="center", y=0.98, yanchor="top"),
        height=430,
        margin=dict(l=0, r=0, t=55, b=0),
        coloraxis_colorbar=dict(title="Population in LEZs"),
        geo=dict(
            projection_type="mercator",
            center=dict(lat=56, lon=8),
            lataxis=dict(range=[40, 75]),
            lonaxis=dict(range=[-42, 27]),
            showcountries=True,
            countrycolor="rgba(80, 80, 80, 0.45)",
            showcoastlines=False,
            showframe=False,
        ),
    )

    st.plotly_chart(fig, width="stretch")
