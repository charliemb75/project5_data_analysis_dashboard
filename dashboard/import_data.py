from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    cars_df = pd.read_csv(DATA_DIR / "cars_processed.csv")

    general_df = (
        pd.read_csv(
            DATA_DIR / "data_general_processed.csv",
            sep=";",
            header=None,
            names=["metric", "value"],
        )
        .set_index("metric")
        .T
        .reset_index(drop=True)
    )

    sales_df = pd.read_csv(
        DATA_DIR / "data_sales_processed.csv",
        sep=";",
        index_col="Country",
    )
    depreciation_df = pd.read_csv(DATA_DIR / "depreciation_processed.csv", sep=";")
    lez_df = pd.read_csv(DATA_DIR / "data_lez.csv", sep=";")
    euro_df = pd.read_csv(
        DATA_DIR / "data_euro_categories.csv",
        sep=";",
        header=None,
        names=["milestone", "date"],
    )

    return cars_df, general_df, sales_df, depreciation_df, lez_df, euro_df
