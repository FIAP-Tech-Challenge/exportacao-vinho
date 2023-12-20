# %% Imports

import polars as pl
import plotly.express as px

# %% #################
# Lendo CSV
######################

df_exp = pl.read_csv("./data/ExpVinho.csv", separator=";", truncate_ragged_lines=True)
df_exp.head()

# %% CSV com código e info dos países
df_pais = pl.read_csv("./data/pais.csv", separator=";", encoding='ISO-8859-1').select(
        pl.col("NO_PAIS_ING").alias("name"),
        pl.col("NO_PAIS").alias("country"),
    )

# %% #################
# Trantando CSV
######################
df_tratado = (
    df_exp.melt(
        id_vars=["Id", "País"],
    )
    .with_columns(
        pl.col("variable")
        .str.extract(r"(\d{4})(_duplicated)?")
        .alias("year")
        .cast(pl.Int64)
    )
    .select(
        pl.col("País").alias("country"),
        pl.col(["year", "value"]),
        pl.when(pl.col("variable").str.contains("_duplicated"))
        .then(pl.lit("value"))
        .otherwise(pl.lit("liters"))
        .alias("type"),
    )
    .pivot(values="value", columns="type", index=["country", "year"])
    .join(df_pais, on="country", how="left")
    .fill_nan(0)
    .fill_null(0)
)

df_tratado.write_csv("./data/dataframe_final.csv")
