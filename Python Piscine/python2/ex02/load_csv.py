import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Make a function that takes a path as argument,
    writes the dimensions of the data set
    and returns it.
    """
    ds = pd.read_csv(path)
    print(f"Loading dataset of dimensions ({ds.shape[0]}, {ds.shape[1]})")
    print(ds)
    return ds
