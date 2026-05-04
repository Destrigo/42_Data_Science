import pandas as pd
import matplotlib.pyplot as mt
from load_csv import load


def main():
    """
    Loads GDP per person and life expectancy data,
    and plots life expectancy vs GDP for each country in 1900.
    """
    # Load datasets
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    # Ensure year 1900 exists
    year = "1900"
    if year not in gdp.columns or year not in life.columns:
        raise ValueError("Year 1900 not found in datasets.")

    # Extract year data
    gdp_1900 = gdp[["country", year]].rename(columns={year: "GDP"})
    life_1900 = life[["country", year]].rename(
        columns={year: "LifeExpectancy"})

    # Merge datasets by country
    merged = pd.merge(gdp_1900, life_1900, on="country", how="inner")

    # Clean and convert GDP strings like "3.28M" or "2B" to floats
    def str_to_float(val):
        if isinstance(val, str):
            if val.endswith("M"):
                return float(val[:-1]) * 1_000_000
            elif val.endswith("B"):
                return float(val[:-1]) * 1_000_000_000
        return float(val)

    merged["GDP"] = merged["GDP"].apply(str_to_float)
    merged["LifeExpectancy"] = pd.to_numeric(merged["LifeExpectancy"],
                                             errors="coerce")

    # Drop invalid rows
    merged = merged.dropna()

    # Plot scatter
    mt.figure(figsize=(10, 6))
    mt.scatter(merged["GDP"], merged["LifeExpectancy"], alpha=0.7,
               color='steelblue', label="Countries")

    # Formatting
    mt.xscale("log")  # GDP often spans several orders of magnitude
    mt.title("Life Expectancy vs GDP per person (PPP, year 1900)")
    mt.xlabel("GDP per person (log scale, $)")
    mt.ylabel("Life Expectancy (years)")
    mt.legend()
    mt.grid(True, which="both", linestyle="--", linewidth=0.5)
    mt.tight_layout()
    mt.show()


if __name__ == "__main__":
    main()
