import numpy as np
import matplotlib.pyplot as mt
from load_csv import load


def main():
    """
    Create a program that calls the load function from the previous
    exercise, loads the file
    life_expectancy_years.csv, and displays the country
    information of your campus. Your
    graph must have a title and a legend for each axis.
    """
    ds = load("life_expectancy_years.csv")
    country = "Netherlands"
    row = ds[ds["country"] == country]
    years = np.array(ds.columns[1:], dtype=int)
    life_exp = row.iloc[0, 1:].to_numpy(dtype=float)

    mt.plot(years, life_exp, linestyle='-',
            color='b', label=country)
    mt.title('Life Expectancy Projections')
    mt.xlabel('Year')
    mt.ylabel('Life expectancy')
    mt.legend()
    mt.show()


if __name__ == "__main__":
    main()
