import numpy as np
import matplotlib.pyplot as mt
from load_csv import load


def str_to_float(val):
    """Convert '3.28M' to 3280000."""
    if isinstance(val, str) and val.endswith('M'):
        return float(val[:-1]) * 1_000_000
    return float(val)


def main():
    """
    Create a program that calls the load function from the
    first exercise, loads the files "in-
    come_per_person_gdppercapita_ppp_inflation_adjusted.csv" and
    "life_expectancy_years.csv",
    and displays the projection of life expectancy in
    relation to the gross national product of
    the year 1900 for each country.
    Your graph must have a title, a legend for each axis
    and a legend for each graph.
    You must display the year 1900.
    """
    ds = load("population_total.csv")

    country = "Netherlands"
    row = ds[ds["country"] == country]
    years = np.array(ds.columns[1:], dtype=int)
    life_exp = row.iloc[0, 1:].apply(str_to_float).to_numpy()

    country2 = "France"
    row2 = ds[ds["country"] == country2]
    life_exp2 = row2.iloc[0, 1:].apply(str_to_float).to_numpy()

    mt.plot(years, life_exp, linestyle='-', color='b', label=country)
    mt.plot(years, life_exp2, linestyle='-', color='r', label=country2)
    mt.title('1900')
    mt.xlabel('Gross domestic product')
    mt.ylabel('Life Expectancy')
    mt.legend()
    mt.show()


if __name__ == "__main__":
    main()
