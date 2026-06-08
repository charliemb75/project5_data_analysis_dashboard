from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pandas as pd


def import_and_preprocess_data(csv_path: Path) -> pd.DataFrame:
    data_year = 2017
    min_year = data_year - 30

    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["mileage", "manufacture_year"])

    df = df[df["manufacture_year"] >= min_year]
    df = df[(df["mileage"] >= 200) & (df["mileage"] <= 500_000)]

    df["age"] = data_year - df["manufacture_year"]
    df_processed = df[["mileage", "age"]]

    summary_df = df_processed[["mileage", "age"]].agg(["mean", "std", "min", "max"]).T
    print(summary_df)

    processed_csv_path = csv_path.with_name(f"{csv_path.stem}_processed{csv_path.suffix}")
    df_processed.to_csv(processed_csv_path, index=False)

    return df_processed


def create_and_save_histogram(
    df: pd.DataFrame,
    variable: str,
    bins: int,
    output_path: Path,
    title: str | None = None,
) -> None:
    plt.figure(figsize=(8, 5))
    plt.hist(df[variable], bins=bins, color="steelblue", edgecolor="black")
    plt.title(title or f"{variable.capitalize()} Distribution")
    plt.xlabel(variable.capitalize())
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def create_and_save_heatmap_plot(
    df: pd.DataFrame,
    x_variable: str,
    y_variable: str,
    output_path: Path,
    title: str | None = None,
    count_threshold: int = 10_000,
    y_bins: int = 70,
) -> None:
    plot_df = df.copy()
    x_min = int(plot_df[x_variable].min())
    x_max = int(plot_df[x_variable].max())
    y_min = plot_df[y_variable].min()
    y_max = plot_df[y_variable].max()
    x_edges = np.arange(x_min - 0.5, x_max + 1.5, 1)
    y_edges = np.linspace(y_min, y_max, y_bins + 1)

    counts, _, _ = np.histogram2d(
        plot_df[x_variable],
        plot_df[y_variable],
        bins=[x_edges, y_edges],
    )

    plt.figure(figsize=(8, 5))
    cmap = plt.cm.viridis.copy()
    cmap.set_under("lightgray")
    mesh = plt.pcolormesh(
        x_edges,
        y_edges,
        counts.T,
        cmap=cmap,
        norm=colors.Normalize(vmin=count_threshold),
        shading="auto",
    )
    plt.title(title or f"{x_variable.capitalize()} vs {y_variable.capitalize()}")
    plt.xlabel(x_variable.capitalize())
    plt.ylabel(y_variable.capitalize())
    plt.colorbar(mesh, label="Count", extend="min")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "cars.csv"

    df = import_and_preprocess_data(csv_path)

    create_and_save_histogram(
        df,
        variable="mileage",
        bins=50,
        output_path=base_dir / "mileage_histogram.png",
        title="Mileage Distribution",
    )
    create_and_save_histogram(
        df,
        variable="age",
        bins=30,
        output_path=base_dir / "age_histogram.png",
        title="Age Distribution",
    )
    create_and_save_heatmap_plot(
        df,
        x_variable="age",
        y_variable="mileage",
        output_path=base_dir / "age_vs_mileage_heatmap.png",
        title="Age vs Mileage Density Heatmap",
    )


if __name__ == "__main__":
    main()
